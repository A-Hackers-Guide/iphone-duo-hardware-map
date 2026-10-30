# `UISDeviceContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `NSCopying`, `NSMutableCopying`
- 1 instance variables, 4 properties, 19 instance methods, 4 class methods

## Instance variables

```
@"NSDictionary" _deviceInfoKeysToValues;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISDeviceContext supportsBSXPCSecureCoding];
+[UISDeviceContext defaultContext];
+[UISDeviceContext _allKeys];
+[UISDeviceContext _keysToValueTypes];
```

## Instance methods

```
-[UISDeviceContext mutableCopyWithZone:];
-[UISDeviceContext _valueTypeForValue:];
-[UISDeviceContext hash];
-[UISDeviceContext description];
-[UISDeviceContext encodeWithBSXPCCoder:];
-[UISDeviceContext initWithBSXPCCoder:];
-[UISDeviceContext copyWithZone:];
-[UISDeviceContext isEqual:];
-[UISDeviceContext deviceInfoFloatValueForKey:];
-[UISDeviceContext deviceInfoIntegerValueForKey:];
-[UISDeviceContext _dictionaryWithOnlyValidKeysFromDictionary:];
-[UISDeviceContext _isDeviceInfoType:appropriateForKey:];
-[UISDeviceContext _isDeviceInfoValue:appropriateForKey:];
-[UISDeviceContext _rawDeviceInfoKeysToValues];
-[UISDeviceContext _valueTypeForKey:];
-[UISDeviceContext deviceInfoBoolValueForKey:];
-[UISDeviceContext deviceInfoStringValueForKey:];
-[UISDeviceContext hasDeviceInfoValueForKey:];
-[UISDeviceContext initWithDeviceInfoValues:];
```
