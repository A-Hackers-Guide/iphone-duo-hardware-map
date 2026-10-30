# `CBABCurveConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _isBuiltin;
B _isEnergySaving;
@"NSString" _uuid;
@"NSNumber" _vendorID;
@"NSNumber" _productID;
@"NSNumber" _maxBrightness;
@"NSNumber" _minBrightness;
```

## Properties

```
@property (T@"NSString",&,N,V_uuid) uuid;
@property (T@"NSNumber",&,N,V_vendorID) vendorID;
@property (T@"NSNumber",&,N,V_productID) productID;
@property (T@"NSNumber",&,N,V_maxBrightness) maxBrightness;
@property (T@"NSNumber",&,N,V_minBrightness) minBrightness;
@property (TB,N,V_isBuiltin) isBuiltin;
@property (TB,N,V_isEnergySaving) isEnergySaving;
```

## Instance methods

```
-[CBABCurveConfiguration vendorID];
-[CBABCurveConfiguration setProductID:];
-[CBABCurveConfiguration productID];
-[CBABCurveConfiguration isBuiltin];
-[CBABCurveConfiguration uuid];
-[CBABCurveConfiguration setVendorID:];
-[CBABCurveConfiguration dealloc];
-[CBABCurveConfiguration setUuid:];
-[CBABCurveConfiguration description];
-[CBABCurveConfiguration copyWithZone:];
-[CBABCurveConfiguration maxBrightness];
-[CBABCurveConfiguration minBrightness];
-[CBABCurveConfiguration setMaxBrightness:];
-[CBABCurveConfiguration setMinBrightness:];
-[CBABCurveConfiguration isEnergySaving];
-[CBABCurveConfiguration setIsBuiltin:];
-[CBABCurveConfiguration setIsEnergySaving:];
```
