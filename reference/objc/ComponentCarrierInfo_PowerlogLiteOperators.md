# `ComponentCarrierInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
i _dlBandwidth;
I _dlEarfcn;
I _dlRfBand;
{?="dlBandwidth"b1"dlEarfcn"b1"dlRfBand"b1} _has;
```

## Properties

```
@property (TB,N) hasDlEarfcn;
@property (TI,N,V_dlEarfcn) dlEarfcn;
@property (TB,N) hasDlBandwidth;
@property (Ti,N,V_dlBandwidth) dlBandwidth;
@property (TB,N) hasDlRfBand;
@property (TI,N,V_dlRfBand) dlRfBand;
```

## Instance methods

```
-[ComponentCarrierInfo writeTo:];
-[ComponentCarrierInfo mergeFrom:];
-[ComponentCarrierInfo hash];
-[ComponentCarrierInfo copyTo:];
-[ComponentCarrierInfo description];
-[ComponentCarrierInfo readFrom:];
-[ComponentCarrierInfo copyWithZone:];
-[ComponentCarrierInfo isEqual:];
-[ComponentCarrierInfo dictionaryRepresentation];
-[ComponentCarrierInfo setDlBandwidth:];
-[ComponentCarrierInfo setHasDlEarfcn:];
-[ComponentCarrierInfo StringAsDlBandwidth:];
-[ComponentCarrierInfo setHasDlRfBand:];
-[ComponentCarrierInfo dlBandwidth];
-[ComponentCarrierInfo dlBandwidthAsString:];
-[ComponentCarrierInfo dlEarfcn];
-[ComponentCarrierInfo dlRfBand];
-[ComponentCarrierInfo hasDlBandwidth];
-[ComponentCarrierInfo hasDlEarfcn];
-[ComponentCarrierInfo hasDlRfBand];
-[ComponentCarrierInfo setDlEarfcn:];
-[ComponentCarrierInfo setDlRfBand:];
-[ComponentCarrierInfo setHasDlBandwidth:];
```
