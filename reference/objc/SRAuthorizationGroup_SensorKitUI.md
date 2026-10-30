# `SRAuthorizationGroup`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 16 properties, 20 instance methods, 2 class methods

## Instance variables

```
@"NSBundle" _bundle;
```

## Properties

```
@property (T@"NSString",R,C) localizedDisplayName;
@property (T@"NSArray",R,C) localizedCollectedData;
@property (T@"NSArray",R,C) localizedNotCollectedData;
@property (T@"NSArray",R,C) localizedWhenShared;
@property (T@"NSArray",R,C) localizedWhatIsShared;
@property (T@"NSString",R,C) localizedDescription;
@property (T@"NSString",R,C) localizedRequiredAuthAlertDetail;
@property (T@"NSString",R,C) localizedRevokeRequiredAuthAlertDetail;
@property (T@"NSString",R,C) localizedPlatforms;
@property (T@"NSArray",R,C) platforms;
@property (T@"NSString",R,C) symbolName;
@property (T@"NSString",R,C) customSymbolName;
@property (T@"UIImage",R,&) illustration;
@property (T@"NSArray",R,C) localizedSampleData;
@property (T@"NSString",R,C) authorizationService;
@property (T@"NSString",R,C) writerAuthorizationService;
```

## Class methods

```
+[SRAuthorizationGroup initialize];
+[SRAuthorizationGroup authorizationGroupWithServiceName:];
```

## Instance methods

```
-[SRAuthorizationGroup localizedDescription];
-[SRAuthorizationGroup symbolName];
-[SRAuthorizationGroup dealloc];
-[SRAuthorizationGroup localizedDisplayName];
-[SRAuthorizationGroup initWithBundle:];
-[SRAuthorizationGroup customSymbolName];
-[SRAuthorizationGroup authorizationService];
-[SRAuthorizationGroup infoPlistAuthorizationCategory];
-[SRAuthorizationGroup writerAuthorizationService];
-[SRAuthorizationGroup illustration];
-[SRAuthorizationGroup localizedCollectedData];
-[SRAuthorizationGroup localizedExampleDataValue:];
-[SRAuthorizationGroup localizedNotCollectedData];
-[SRAuthorizationGroup localizedPlatforms];
-[SRAuthorizationGroup localizedRequiredAuthAlertDetail];
-[SRAuthorizationGroup localizedRevokeRequiredAuthAlertDetail];
-[SRAuthorizationGroup localizedSampleData];
-[SRAuthorizationGroup localizedWhatIsShared];
-[SRAuthorizationGroup localizedWhenShared];
-[SRAuthorizationGroup platforms];
```
