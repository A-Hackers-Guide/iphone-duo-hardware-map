# `BLSHEnvironmentDateInterval`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _shouldReset;
@"NSDateInterval" _presentationInterval;
@"NSDate" _previousPresentationDate;
@"<BLSHBacklightSceneHostEnvironment>" _environment;
```

## Properties

```
@property (T@"NSDateInterval",R,N,V_presentationInterval) presentationInterval;
@property (T@"NSDate",R,N,V_previousPresentationDate) previousPresentationDate;
@property (TB,R,N,V_shouldReset) shouldReset;
@property (T@"<BLSHBacklightSceneHostEnvironment>",R,N,V_environment) environment;
```

## Class methods

```
+[BLSHEnvironmentDateInterval intervalWithPresentationInterval:previousPresentationDate:shouldReset:environment:];
```

## Instance methods

```
-[BLSHEnvironmentDateInterval hash];
-[BLSHEnvironmentDateInterval description];
-[BLSHEnvironmentDateInterval isEqual:];
-[BLSHEnvironmentDateInterval environment];
-[BLSHEnvironmentDateInterval presentationInterval];
-[BLSHEnvironmentDateInterval shouldReset];
-[BLSHEnvironmentDateInterval initWithPresentationInterval:previousPresentationDate:shouldReset:environment:];
-[BLSHEnvironmentDateInterval previousPresentationDate];
```
