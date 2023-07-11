# Databricks notebook source
import pandas as pd
import numpy as np
from scipy import fft
import copy

def create_calendar_df(min_date, max_date):
    dates = list(pd.date_range(min_date, max_date, freq='d'))
    dates = [d.date() for d in dates]
    dates_df = pd.DataFrame(dates, columns=['date'])
    dates_df.index = dates_df.date
    dates_df = dates_df.drop(columns=['date'], axis=1)
    return dates_df

def closest_enum(period):
    pass
