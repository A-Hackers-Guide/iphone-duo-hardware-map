# `UISActivityContinuationAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSAction`
- 0 instance variables, 7 properties, 12 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) activityTypeIdentifier;
@property (T@"NSString",R,N) originatingDeviceType;
@property (T@"NSString",R,N) originatingDeviceName;
@property (T@"NSString",R,N) activityType;
@property (T@"NSDate",R,N) lastUpdateTime;
@property (T@"NSData",R,N) userActivityData;
```

## Class methods

```
+[UISActivityContinuationAction buildWithUserActivity:completion:];
```

## Instance methods

```
-[UISActivityContinuationAction lastUpdateTime];
-[UISActivityContinuationAction UIActionType];
-[UISActivityContinuationAction identifier];
-[UISActivityContinuationAction abortForUsageViolation:];
-[UISActivityContinuationAction activityType];
-[UISActivityContinuationAction keyDescriptionForSetting:];
-[UISActivityContinuationAction originatingDeviceName];
-[UISActivityContinuationAction userActivityData];
-[UISActivityContinuationAction isKindOfClass:];
-[UISActivityContinuationAction initWithSettings:];
-[UISActivityContinuationAction activityTypeIdentifier];
-[UISActivityContinuationAction originatingDeviceType];
```
