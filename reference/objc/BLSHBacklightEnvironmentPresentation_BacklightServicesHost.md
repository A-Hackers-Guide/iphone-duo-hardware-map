# `BLSHBacklightEnvironmentPresentation`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _presentationEntries;
@"BLSHFlipbookContext" _flipbookContext;
@"NSDate" _expirationDate;
@"NSSet" _environmentsSet;
```

## Properties

```
@property (T@"BLSHPresentationDateSpecifier",R,N) currentSpecifier;
@property (T@"NSSet",R,N,V_environmentsSet) environmentsSet;
@property (T@"NSArray",R,C,N,V_presentationEntries) presentationEntries;
@property (T@"NSArray",R,C,N) environments;
@property (T@"CAContext",R,N) caContext;
@property (T@"BLSHFlipbookContext",R,N,V_flipbookContext) flipbookContext;
@property (T@"NSDate",R,C,N,V_expirationDate) expirationDate;
@property (TB,R,GisLiveUpdating) liveUpdating;
@property (TB,R,GhasUnrestrictedFramerateUpdates) unrestrictedFramerateUpdates;
@property (TB,R,GisHighLuminanceAlwaysOn) highLuminanceAlwaysOn;
@property (TB,R) wantsLowPowerRendering;
```

## Instance methods

```
-[BLSHBacklightEnvironmentPresentation bls_loggingString];
-[BLSHBacklightEnvironmentPresentation bls_shortLoggingString];
-[BLSHBacklightEnvironmentPresentation debugDescription];
-[BLSHBacklightEnvironmentPresentation expirationDate];
-[BLSHBacklightEnvironmentPresentation currentSpecifier];
-[BLSHBacklightEnvironmentPresentation differenceFromPresentation:forEachRemoval:forEachAddition:];
-[BLSHBacklightEnvironmentPresentation environments];
-[BLSHBacklightEnvironmentPresentation initWithPresentationEntries:flipbookContext:expirationDate:];
-[BLSHBacklightEnvironmentPresentation initWithEnvironments:caContext:expirationDate:];
-[BLSHBacklightEnvironmentPresentation isHighLuminanceAlwaysOn];
-[BLSHBacklightEnvironmentPresentation hasUnrestrictedFramerateUpdates];
-[BLSHBacklightEnvironmentPresentation invalidateContentForReason:];
-[BLSHBacklightEnvironmentPresentation containsEnvironment:];
-[BLSHBacklightEnvironmentPresentation initWithFBScenes:flipbookContext:expirationDate:];
-[BLSHBacklightEnvironmentPresentation caContext];
-[BLSHBacklightEnvironmentPresentation hash];
-[BLSHBacklightEnvironmentPresentation description];
-[BLSHBacklightEnvironmentPresentation presentationEntries];
-[BLSHBacklightEnvironmentPresentation differenceFromPresentation:];
-[BLSHBacklightEnvironmentPresentation environmentsSet];
-[BLSHBacklightEnvironmentPresentation isEqual:];
-[BLSHBacklightEnvironmentPresentation isLiveUpdating];
-[BLSHBacklightEnvironmentPresentation flipbookContext];
-[BLSHBacklightEnvironmentPresentation wantsLowPowerRendering];
-[BLSHBacklightEnvironmentPresentation initWithPresentationEntries:caContext:expirationDate:];
```
