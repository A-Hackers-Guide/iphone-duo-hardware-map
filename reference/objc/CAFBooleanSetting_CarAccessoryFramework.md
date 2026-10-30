# `CAFBooleanSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 12 properties, 23 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFUserVisibleDetailedDescriptionCharacteristic",R,N) userVisibleDetailedDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFBooleanSettingNotificationEntryCharacteristic",R,N) booleanNotificationInfoCharacteristic;
@property (TB,N) on;
@property (TB,R,N) onRestricted;
@property (T@"CAFUserVisibleDetailedDescription",R,N) userVisibleDetailedDescription;
@property (TB,R,N) hasUserVisibleDetailedDescription;
@property (T@"NSString",R,N) userVisibleDescription;
@property (TB,R,N) hasUserVisibleDescription;
@property (T@"CAFBooleanSettingNotificationEntry",R,N) booleanNotificationInfo;
@property (TB,R,N) hasBooleanNotificationInfo;
```

## Class methods

```
+[CAFBooleanSetting serviceIdentifier];
+[CAFBooleanSetting observerProtocol];
```

## Instance methods

```
-[CAFBooleanSetting on];
-[CAFBooleanSetting removeObserver:];
-[CAFBooleanSetting addObserver:];
-[CAFBooleanSetting setOn:];
-[CAFBooleanSetting registerObserver:];
-[CAFBooleanSetting name];
-[CAFBooleanSetting unregisterObserver:];
-[CAFBooleanSetting registeredForOn];
-[CAFBooleanSetting booleanNotificationInfo];
-[CAFBooleanSetting onRestricted];
-[CAFBooleanSetting registeredForBooleanNotificationInfo];
-[CAFBooleanSetting registeredForUserVisibleDescription];
-[CAFBooleanSetting registeredForUserVisibleDetailedDescription];
-[CAFBooleanSetting userVisibleDescription];
-[CAFBooleanSetting userVisibleDetailedDescription];
-[CAFBooleanSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFBooleanSetting booleanNotificationInfoCharacteristic];
-[CAFBooleanSetting hasBooleanNotificationInfo];
-[CAFBooleanSetting hasUserVisibleDescription];
-[CAFBooleanSetting hasUserVisibleDetailedDescription];
-[CAFBooleanSetting onCharacteristic];
-[CAFBooleanSetting userVisibleDescriptionCharacteristic];
-[CAFBooleanSetting userVisibleDetailedDescriptionCharacteristic];
```
