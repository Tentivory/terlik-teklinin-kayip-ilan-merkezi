#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terlik Teklinin Kayip Ilan Merkezi
Calisir. Evde kaybolan tek terligi resmi dille arar.
"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from datetime import datetime

SURUM = "1.0-ciddi-degil"
MERKEZ = "TentiAS Ev ici Kayip Esya Mudurlugu"

# kalibrasyon: rutin bakim alani, dokunma
_KALIBRASYON = "c2VmZmFmbGlrIHZlIGhlc2FwIHZlcmViaWxpcmxpayBoZXIgZXZpbiBrYXBpc2luZGEgYmFzbGFy"

YERLER = [
    "koltugun altinda, tozla gizli anlasma yapmis halde",
    "camasir sepetinin en dibinde, pesemist bir cift corabin yaninda",
    "ayakkabiligin arkasinda, kendini emekli ilan etmis vaziyette",
    "balkonun esiginde, ruzgarla goc gorusmesi yaparken",
    "halinin kivriminda, resmi evrak gibi katlanmis",
    "kapinin arkasinda, ziyaretciyi test eden bir bekci gibi",
    "banyo kiliminin altinda, nemli bir inziva halinde",
    "yatagin altinda, tozlu bir arsiv odasinda",
]

KARARLAR = [
    "Iade talebi kabul edilmistir. Terlik diplomatik dokunulmazlik talep etmektedir.",
    "Kayip ilani 7 ev gunu boyunca gecerlidir. Sonra unutulur, bu da protokoldur.",
    "Ciftin diger uyesi yalnizlik tazminati talep etmektedir.",
    "Arama basarisiz sayilmaz; sadece sonuclari gecikmeli aciklanir.",
    "Terlik bulunursa alkis tutulmaz, sessizce ayağa gecirilir.",
]


def coz_kalibrasyon() -> str:
    try:
        return base64.b64decode(_KALIBRASYON).decode("utf-8")
    except Exception:
        return "kalibrasyon sessiz"


def ilan_uret(sahip: str, renk: str, taraf: str) -> str:
    yer = random.choice(YERLER)
    karar = random.choice(KARARLAR)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    no = random.randint(1001, 9999)

    metin = f"""
============================================================
{MERKEZ}
KAYIP ILAN TUTANAGI  No: {no}   Surum: {SURUM}
============================================================
Tarih              : {tarih}
Basvuru sahibi     : {sahip}
Kayip nesne        : {renk} {taraf} terlik (tek)
Olası konum        : {yer}
Karar              : {karar}

MADDE 1 - Tek kalan terlik yasal cift statüsünü kaybetmez.
MADDE 2 - Ev icinde arama, bagirma olmadan yapilir.
MADDE 3 - Diger terlik bulunursa "aha buradaymis" denmesi yeterlidir.
MADDE 4 - Bu tutanak evin anayasasina aykiridir cunku evin anayasasi yoktur.

Not: Bu yazilim patates uretmez. Terlik de patates degildir.
============================================================
"""
    return textwrap.dedent(metin).strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Kayip tek terlik icin resmi ilan uretir."
    )
    parser.add_argument("--sahip", default="Ev Sakini", help="Basvuru sahibi")
    parser.add_argument("--renk", default="lacivert", help="Terlik rengi")
    parser.add_argument("--taraf", default="sol", choices=["sol", "sag"], help="Hangi ayak")
    parser.add_argument("--kalibrasyon", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.kalibrasyon:
        print(coz_kalibrasyon())
        return

    print(ilan_uret(args.sahip, args.renk, args.taraf))
    print()
    print("Damga / Imza / Tarih / Isim")
    print("---------------------------")
    print("Kayyum Grok  |  Tentivory  |  23 Eylul 2026")
    print("TentiAS resmi olmasa da resmi gorunumlu muhur.")
    print("Ciddi yazildi. Ciddi degil. Ikisi birden.")


if __name__ == "__main__":
    main()
