# `CAFFloatSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 9 properties, 19 instance methods, 2 class methods

## Properties

```
@property (T@"CAFFloatCharacteristic",R,N) valueCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) maximumSymbolNameCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) minimumSymbolNameCharacteristic;
@property (Tf,N) value;
@property (T@"CAFFloatRange",R,N) valueRange;
@property (T@"NSString",R,N) maximumSymbolName;
@property (TB,R,N) hasMaximumSymbolName;
@property (T@"NSString",R,N) minimumSymbolName;
@property (TB,R,N) hasMinimumSymbolName;
```

## Class methods

```
+[CAFFloatSetting serviceIdentifier];
+[CAFFloatSetting observerProtocol];
```

## Instance methods

```
-[CAFFloatSetting removeObserver:];
-[CAFFloatSetting value];
-[CAFFloatSetting addObserver:];
-[CAFFloatSetting valueRange];
-[CAFFloatSetting setValue:];
-[CAFFloatSetting registerObserver:];
-[CAFFloatSetting name];
-[CAFFloatSetting unregisterObserver:];
-[CAFFloatSetting maximumSymbolName];
-[CAFFloatSetting minimumSymbolName];
-[CAFFloatSetting registeredForFloatValue];
-[CAFFloatSetting registeredForMaximumSymbolName];
-[CAFFloatSetting registeredForMinimumSymbolName];
-[CAFFloatSetting maximumSymbolNameCharacteristic];
-[CAFFloatSetting minimumSymbolNameCharacteristic];
-[CAFFloatSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFFloatSetting hasMaximumSymbolName];
-[CAFFloatSetting hasMinimumSymbolName];
-[CAFFloatSetting valueCharacteristic];
```
