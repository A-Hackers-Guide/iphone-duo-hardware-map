# `UISUserInterfaceStyleMode`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<UISUserInterfaceStyleModeDelegate>" _delegate;
B _observingDefaults;
```

## Properties

```
@property (Tq,N) modeValue;
@property (Tq,R,N) suggestedAutomaticModeValue;
@property (T{?=qq},N) override;
@property (T{?={?=qq}{?=qq}},N) customSchedule;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISUserInterfaceStyleMode initWithDelegate:];
-[UISUserInterfaceStyleMode observeValueForKeyPath:ofObject:change:context:];
-[UISUserInterfaceStyleMode debugDescription];
-[UISUserInterfaceStyleMode succinctDescriptionBuilder];
-[UISUserInterfaceStyleMode dealloc];
-[UISUserInterfaceStyleMode descriptionWithMultilinePrefix:];
-[UISUserInterfaceStyleMode succinctDescription];
-[UISUserInterfaceStyleMode description];
-[UISUserInterfaceStyleMode descriptionBuilderWithMultilinePrefix:];
-[UISUserInterfaceStyleMode customSchedule];
-[UISUserInterfaceStyleMode modeValue];
-[UISUserInterfaceStyleMode override];
-[UISUserInterfaceStyleMode setModeValue:];
-[UISUserInterfaceStyleMode setOverride:];
-[UISUserInterfaceStyleMode _commonAnalyticsEventDictionary];
-[UISUserInterfaceStyleMode _setOverride:force:];
-[UISUserInterfaceStyleMode setCustomSchedule:];
-[UISUserInterfaceStyleMode suggestedAutomaticModeValue];
```
