# `CAFIntegerSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 21 properties, 35 instance methods, 2 class methods

## Properties

```
@property (T@"CAFInt32Characteristic",R,N) valueCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleValueCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFUserVisibleDetailedDescriptionCharacteristic",R,N) userVisibleDetailedDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) maximumSymbolNameCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) minimumSymbolNameCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) stepperBarHiddenCharacteristic;
@property (Ti,N) value;
@property (T@"CAFInt32Range",R,N) valueRange;
@property (T@"NSString",R,N) userVisibleValue;
@property (TB,R,N) hasUserVisibleValue;
@property (T@"NSString",R,N) userVisibleDescription;
@property (TB,R,N) hasUserVisibleDescription;
@property (T@"CAFUserVisibleDetailedDescription",R,N) userVisibleDetailedDescription;
@property (TB,R,N) hasUserVisibleDetailedDescription;
@property (T@"NSString",R,N) maximumSymbolName;
@property (TB,R,N) hasMaximumSymbolName;
@property (T@"NSString",R,N) minimumSymbolName;
@property (TB,R,N) hasMinimumSymbolName;
@property (TB,R,N) stepperBarHidden;
@property (TB,R,N) hasStepperBarHidden;
```

## Class methods

```
+[CAFIntegerSetting serviceIdentifier];
+[CAFIntegerSetting observerProtocol];
```

## Instance methods

```
-[CAFIntegerSetting removeObserver:];
-[CAFIntegerSetting value];
-[CAFIntegerSetting addObserver:];
-[CAFIntegerSetting valueRange];
-[CAFIntegerSetting setValue:];
-[CAFIntegerSetting registerObserver:];
-[CAFIntegerSetting name];
-[CAFIntegerSetting unregisterObserver:];
-[CAFIntegerSetting hasStepperBarHidden];
-[CAFIntegerSetting maximumSymbolName];
-[CAFIntegerSetting minimumSymbolName];
-[CAFIntegerSetting registeredForInt32Value];
-[CAFIntegerSetting registeredForMaximumSymbolName];
-[CAFIntegerSetting registeredForMinimumSymbolName];
-[CAFIntegerSetting registeredForStepperBarHidden];
-[CAFIntegerSetting registeredForUserVisibleDescription];
-[CAFIntegerSetting registeredForUserVisibleDetailedDescription];
-[CAFIntegerSetting registeredForUserVisibleValue];
-[CAFIntegerSetting stepperBarHidden];
-[CAFIntegerSetting userVisibleDescription];
-[CAFIntegerSetting userVisibleDetailedDescription];
-[CAFIntegerSetting userVisibleValue];
-[CAFIntegerSetting hasUserVisibleValue];
-[CAFIntegerSetting maximumSymbolNameCharacteristic];
-[CAFIntegerSetting minimumSymbolNameCharacteristic];
-[CAFIntegerSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFIntegerSetting hasMaximumSymbolName];
-[CAFIntegerSetting hasMinimumSymbolName];
-[CAFIntegerSetting hasUserVisibleDescription];
-[CAFIntegerSetting hasUserVisibleDetailedDescription];
-[CAFIntegerSetting stepperBarHiddenCharacteristic];
-[CAFIntegerSetting userVisibleDescriptionCharacteristic];
-[CAFIntegerSetting userVisibleDetailedDescriptionCharacteristic];
-[CAFIntegerSetting userVisibleValueCharacteristic];
-[CAFIntegerSetting valueCharacteristic];
```
