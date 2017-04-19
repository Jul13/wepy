# -*- coding: utf-8 -*-
# Author: Joel Bun and Anis Al Gerbi
import numpy as np
import pandas as pd
import datetime as dat
import topyc.io.Map as Map


class Mat2Df:
    def __init__(self, data_dict, additional_keys=None):
        if additional_keys is None:
            additional_keys = []
        self.__convert_date(data_dict)
        self.__dict_univ(data_dict)
        self.__df_assets(data_dict)
        keys = ['Weights', 'VolumesCcy'] + additional_keys
        dict_ = {'Returns': self.__get_tables(data_dict, 'Returns')}
        for k in keys:
            dict_[k] = self.__get_tables(data_dict, k)
        self.Tables = Map.Map(dict_)
        del dict_
        # self.__df_returns(data_dict);
        # self.__df_volumes(data_dict);
        # self.__df_weights(data_dict);
        self.T = self.Tables.Returns.shape[0]
        self.N = self.Tables.Returns.shape[1]

    def __convert_date(self, data_dict):
        self.dates = []
        for i in range(len(data_dict['Dates'])):
            self.dates.append(dat.datetime.fromordinal(int(data_dict['Dates'][i][0])) +
                              dat.timedelta(days=int(data_dict['Dates'][i][0]) % 1) - dat.timedelta(days=366))

    def __dict_univ(self, data_dict):
        self.univ = {n: data_dict['Univ'][n][0, 0][0] for n in data_dict['Univ'].dtype.names}

    def __df_assets(self, data_dict):
        d = {}
        mdtype = data_dict['Assets'].dtype
        for j in range(data_dict['Assets'].shape[0]):
            d[j] = {}
            for n in mdtype.names:
                if ('int' in str(data_dict['Assets'][n][j, 0].dtype)) or (
                            'float' in str(data_dict['Assets'][n][j, 0].dtype)):
                    d[j][n] = data_dict['Assets'][n][j, 0][0][0]
                else:
                    d[j][n] = data_dict['Assets'][n][j, 0][0]
        self.Assets = pd.DataFrame.from_dict(d)
        self.Assets.columns = self.Assets.loc['Id_Bbg']

    def __get_tables(self, data_dict, key):
        df = pd.DataFrame(np.array(data_dict[key]))
        if df.shape[0] == len(self.dates):
            df.drop(df.index[0], inplace=True)
        df.set_index(pd.DatetimeIndex(self.dates[1:len(self.dates)]), inplace='True')
        df.columns = self.Assets.columns  # [self.Assets.index == 'Name'].T.Name;
        return df

        # def __df_returns(self, data_dict):
        #     self.returns = pd.DataFrame(data=data_dict['Returns']);
        #     self.returns.set_index(pd.DatetimeIndex(self.dates[1:len(self.dates)]), inplace='True');
        #     self.returns.columns = self.assets[self.assets.index == 'Name'].T.Name;
        #
        # def __df_volumes(self, data_dict):
        #     self.volumes = pd.DataFrame(data=data_dict['VolumesCcy']);
        #     self.volumes.set_index(pd.DatetimeIndex(self.dates), inplace='True');
        #     self.volumes.columns = self.assets[self.assets.index == 'Name'].T.Name;
        #
        # def __df_weights(self, data_dict):
        #     self.weights = pd.DataFrame(data=data_dict['Weights']);
        #     self.weights.set_index(pd.DatetimeIndex(self.dates), inplace='True');
        #     self.weights.columns = self.assets[self.assets.index == 'Name'].T.Name;


class Mat2dfV73:
    """A comment is needed here."""

    def __init__(self, data_hdf, additional_keys=None):
        """A comment is needed here."""
        if additional_keys is None:
            additional_keys = []
        self.__convert_date(data_hdf)
        self.__dict_univ(data_hdf)
        self.__df_assets(data_hdf)
        keys = ['Weights', 'VolumesCcy'] + additional_keys
        dict_ = {'Returns': self.__get_tables(data_hdf, 'Returns')}
        for k in keys:
            dict_[k] = self.__get_tables(data_hdf, k)
        self.Tables = Map.Map(dict_)
        del dict_
        self.T = self.Tables.Returns.shape[0]
        self.N = self.Tables.Returns.shape[1]

    def __convert_date(self, data_hdf):
        """A comment is needed here."""
        self.dates = []
        date_array = np.array(data_hdf['Dates']).T
        for i in range(date_array.shape[0]):
            self.dates.append(dat.datetime.fromordinal(int(date_array[i]))
                              + dat.timedelta(days=int(date_array[i]) % 1)
                              - dat.timedelta(days=366))

    def __dict_univ(self, data_hdf):
        self.univ = {n: ''.join(map(chr, data_hdf['Univ'][n].value))
                     for n in data_hdf['Univ'].keys()}

    def __df_assets(self, data_hdf):
        d = {}
        keys = ['Name', 'Id_Bbg', 'Bbg_CloseTime', 'Bbg_CountryTrading',
                'Bbg_Sector']
        # mdtype = data_hdf['Assets'].dtype
        # for j in range(data_hdf['Assets'].shape[0]):
        for j in range(data_hdf['Returns'].shape[0]):
            d[j] = {}
            # for n in data_hdf['Assets'].keys():
            for n in keys:
                try:
                    if np.array(data_hdf[data_hdf['Assets'][n].value[0][j]]).shape[0] > 1:
                        d[j][n] = ''.join(map(chr, np.array(data_hdf[
                                                                data_hdf['Assets'][n].value[0][j]])))
                    else:
                        d[j][n] = np.array(data_hdf[data_hdf['Assets'][n]
                                           .value[0][j]])[0][0]
                except:
                    d[j][n] = np.array(data_hdf[data_hdf['Assets']['Bbg_CloseTime']
                                       .value[0][1]])[0][0]
                    pass
        self.Assets = pd.DataFrame.from_dict(d)
        self.Assets.columns = self.Assets.loc['Id_Bbg']

    def __get_tables(self, data_hdf, key):
        df = pd.DataFrame(np.array(data_hdf[key]).T)
        if df.shape[0] == len(self.dates):
            df.drop(df.index[0], inplace=True)
        df.set_index(pd.DatetimeIndex(self.dates[1:len(self.dates)]),
                     inplace='True')
        # [self.Assets.index == 'Name'].T.Name
        df.columns = self.Assets.columns
        return df


"""
    def __df_returns(self, data_hdf):
        self.returns = ;
        self.returns.set_index(pd.DatetimeIndex(self.dates[1:len(self.dates)]),
                               inplace='True');
        self.returns.columns = self.assets[self.assets.index == 'Name'].T.Name;

    def __df_volumes(self, data_hdf):
        self.volumes = pd.DataFrame(np.array(data_hdf['VolumesCcy']).T);
        self.volumes.set_index(pd.DatetimeIndex(self.dates), inplace='True');
        self.volumes.columns = self.assets[self.assets.index == 'Name'].T.Name;

    def __df_weights(self, data_hdf):
        self.weights = pd.DataFrame(np.array(data_hdf['Weights']).T);
        self.weights.set_index(pd.DatetimeIndex(self.dates), inplace='True');
        self.weights.columns = self.assets[self.assets.index == 'Name'].T.Name;
"""
