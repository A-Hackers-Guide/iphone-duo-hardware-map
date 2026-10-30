# `BLSAlwaysOnSession`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 2 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<BLSBacklightSceneEnvironment>" _environment;
@"BLSFrameSpecifierModel" _model;
```

## Properties

```
@property (T@"BLSFrameSpecifierModel",&,V_model) model;
@property (T@"<BLSBacklightSceneEnvironment>",R,W,V_environment) environment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSAlwaysOnSession model];
-[BLSAlwaysOnSession setModel:];
-[BLSAlwaysOnSession initWithEnvironment:];
-[BLSAlwaysOnSession invalidate];
-[BLSAlwaysOnSession description];
-[BLSAlwaysOnSession environment];
-[BLSAlwaysOnSession desiredFidelityForDateInterval:timelines:withCompletion:];
-[BLSAlwaysOnSession performFrameSpecifiersRequest:timelines:];
-[BLSAlwaysOnSession specifierForPresentationDate:];
```
