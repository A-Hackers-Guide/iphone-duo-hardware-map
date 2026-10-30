# `CTBandInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _fActiveBands;
@"NSMutableDictionary" _fSupportedBands;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_fActiveBands) fActiveBands;
@property (T@"NSMutableDictionary",&,N,V_fSupportedBands) fSupportedBands;
```

## Class methods

```
+[CTBandInfo supportsSecureCoding];
```

## Instance methods

```
-[CTBandInfo init];
-[CTBandInfo supportedBands];
-[CTBandInfo encodeWithCoder:];
-[CTBandInfo description];
-[CTBandInfo initWithCoder:];
-[CTBandInfo copyWithZone:];
-[CTBandInfo isEqual:];
-[CTBandInfo fSupportedBands];
-[CTBandInfo activeBands];
-[CTBandInfo activeBandsForRat:];
-[CTBandInfo addActiveBand:forRat:];
-[CTBandInfo addActiveBands:forRat:];
-[CTBandInfo addSupportedBand:forRat:];
-[CTBandInfo addSupportedBands:forRat:];
-[CTBandInfo fActiveBands];
-[CTBandInfo initWithActiveBands:];
-[CTBandInfo initWithSupported:andActiveBands:];
-[CTBandInfo initWithSupportedBands:];
-[CTBandInfo setFActiveBands:];
-[CTBandInfo setFSupportedBands:];
-[CTBandInfo supportedBandsForRat:];
```
