#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil

import requests
from flask import render_template, flash, request, current_app, Response
from flask_login import login_required

from . import main
from .forms import *
from ..fuc import *
from flask_moment import datetime


@main.route('/', methods=['POST', 'GET'])
def index():
    form1 = HexStr2BinStrForm()
    if form1.submit1.data and form1.validate_on_submit():
        flash(hexStr2BinStr(form1.hex_str.data))
    form2 = Dec2BinStrForm()
    if form2.bits_of_digit.data is None:
        form2.bits_of_digit.data = 8
    if form2.submit2.data and form2.validate_on_submit():
        flash(dec2BinStr(form2.dec.data, form2.bits_of_digit.data))
    form3 = BinStr2DecForm()
    if form3.submit3.data and form3.validate_on_submit():
        flash(binStr2Dec(form3.bin_str.data))
    form4 = HexStr2DecForm()
    if form4.submit4.data and form4.validate_on_submit():
        flash(hexStr2Dec(form4.hex_str.data))
    form5 = ComplementBinStr2DecForm()
    if form5.submit5.data and form5.validate_on_submit():
        flash(complementBinStr2Dec(form5.bin_str.data))
    form6 = Dec2ComplementBinStrForm()
    if form6.bits_of_digit.data is None:
        form6.bits_of_digit.data = 16
    if form6.submit6.data and form6.validate_on_submit():
        flash(Dec2ComplementBinStr(form6.dec.data, form6.bits_of_digit.data))
    form7 = StrLengthForm()
    if form7.submit7.data and form7.validate_on_submit():
        flash(len(form7.num_str.data))
    form8 = BinStr2HexStrForm()
    if form8.submit8.data and form8.validate_on_submit():
        flash(BinStr2HexStr(form8.bin_str.data))
    form9 = CalculatorForm()
    if form9.submit9.data and form9.validate_on_submit():
        flash(cal(form9.calculator_str.data))
    forms = [form2, form6, form5, form3, form8, form1, form4, form7]
    return render_template('index.html', forms=forms)

