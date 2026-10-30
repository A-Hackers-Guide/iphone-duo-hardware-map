# `CBTDSScanRequest`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `CUXPCCodable`, `NSCopying`
- 3 instance variables, 3 properties, 18 instance methods, 1 class methods

## Instance variables

```
C _filterMode;
@"NSArray" _filterRules;
@"NSSet" _allTIKs;
```

## Properties

```
@property (TC,N,V_filterMode) filterMode;
@property (T@"NSSet",C,N,V_allTIKs) allTIKs;
@property (T@"NSArray",C,N,V_filterRules) filterRules;
```

## Class methods

```
+[CBTDSScanRequest supportsSecureCoding];
```

## Instance methods

```
-[CBTDSScanRequest encodeWithXPCObject:];
-[CBTDSScanRequest initWithXPCObject:error:];
-[CBTDSScanRequest descriptionWithLevel:];
-[CBTDSScanRequest init];
-[CBTDSScanRequest encodeWithCoder:];
-[CBTDSScanRequest hash];
-[CBTDSScanRequest description];
-[CBTDSScanRequest initWithCoder:];
-[CBTDSScanRequest filterMode];
-[CBTDSScanRequest copyWithZone:];
-[CBTDSScanRequest isEqual:];
-[CBTDSScanRequest setFilterMode:];
-[CBTDSScanRequest setFilterRules:];
-[CBTDSScanRequest allTIKs];
-[CBTDSScanRequest _ruleContainsScreenOffFlag];
-[CBTDSScanRequest filterRules];
-[CBTDSScanRequest isClassDataValid];
-[CBTDSScanRequest setAllTIKs:];
```
