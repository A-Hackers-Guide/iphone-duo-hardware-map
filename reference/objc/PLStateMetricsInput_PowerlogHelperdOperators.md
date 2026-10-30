# `PLStateMetricsInput`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 24 properties, 48 instance methods, 0 class methods

## Instance variables

```
d _foregroundTimeSeconds;
d _backgroundTimeSeconds;
d _backgroundAudioTimeSeconds;
d _backgroundLocationTimeSeconds;
d _locationBestAccuracySeconds;
d _locationBestAccuracyNavSeconds;
d _locationTenMetersSeconds;
d _locationHundredMetersSeconds;
d _locationKilometerSeconds;
d _locationThreeKilometersSeconds;
d _locationReducedAccuracySeconds;
@"NSDictionary" _cellularConditionHistogram;
@"NSArray" _foregroundLaunchDurations;
@"NSArray" _backgroundLaunchDurations;
@"NSArray" _extendedLaunchDurations;
@"NSArray" _resumeDurations;
@"NSArray" _hangDurations;
@"NSArray" _activationLaunchDurations;
@"NSArray" _activationAfterPrewarmDurations;
@"NSDictionary" _scrollGlitches;
@"NSDictionary" _foregroundExits;
@"NSDictionary" _backgroundExits;
@"NSDictionary" _signpostIntervals;
@"NSArray" _metalFrameRate;
```

## Properties

```
@property (Td,N,V_foregroundTimeSeconds) foregroundTimeSeconds;
@property (Td,N,V_backgroundTimeSeconds) backgroundTimeSeconds;
@property (Td,N,V_backgroundAudioTimeSeconds) backgroundAudioTimeSeconds;
@property (Td,N,V_backgroundLocationTimeSeconds) backgroundLocationTimeSeconds;
@property (Td,N,V_locationBestAccuracySeconds) locationBestAccuracySeconds;
@property (Td,N,V_locationBestAccuracyNavSeconds) locationBestAccuracyNavSeconds;
@property (Td,N,V_locationTenMetersSeconds) locationTenMetersSeconds;
@property (Td,N,V_locationHundredMetersSeconds) locationHundredMetersSeconds;
@property (Td,N,V_locationKilometerSeconds) locationKilometerSeconds;
@property (Td,N,V_locationThreeKilometersSeconds) locationThreeKilometersSeconds;
@property (Td,N,V_locationReducedAccuracySeconds) locationReducedAccuracySeconds;
@property (T@"NSDictionary",C,N,V_cellularConditionHistogram) cellularConditionHistogram;
@property (T@"NSArray",C,N,V_foregroundLaunchDurations) foregroundLaunchDurations;
@property (T@"NSArray",C,N,V_backgroundLaunchDurations) backgroundLaunchDurations;
@property (T@"NSArray",C,N,V_extendedLaunchDurations) extendedLaunchDurations;
@property (T@"NSArray",C,N,V_resumeDurations) resumeDurations;
@property (T@"NSArray",C,N,V_hangDurations) hangDurations;
@property (T@"NSArray",C,N,V_activationLaunchDurations) activationLaunchDurations;
@property (T@"NSArray",C,N,V_activationAfterPrewarmDurations) activationAfterPrewarmDurations;
@property (T@"NSDictionary",C,N,V_scrollGlitches) scrollGlitches;
@property (T@"NSDictionary",C,N,V_foregroundExits) foregroundExits;
@property (T@"NSDictionary",C,N,V_backgroundExits) backgroundExits;
@property (T@"NSDictionary",C,N,V_signpostIntervals) signpostIntervals;
@property (T@"NSArray",C,N,V_metalFrameRate) metalFrameRate;
```

## Instance methods

```
-[PLStateMetricsInput setSignpostIntervals:];
-[PLStateMetricsInput signpostIntervals];
-[PLStateMetricsInput activationAfterPrewarmDurations];
-[PLStateMetricsInput foregroundExits];
-[PLStateMetricsInput resumeDurations];
-[PLStateMetricsInput setLocationBestAccuracySeconds:];
-[PLStateMetricsInput backgroundExits];
-[PLStateMetricsInput activationLaunchDurations];
-[PLStateMetricsInput backgroundAudioTimeSeconds];
-[PLStateMetricsInput backgroundLaunchDurations];
-[PLStateMetricsInput backgroundLocationTimeSeconds];
-[PLStateMetricsInput backgroundTimeSeconds];
-[PLStateMetricsInput cellularConditionHistogram];
-[PLStateMetricsInput extendedLaunchDurations];
-[PLStateMetricsInput foregroundLaunchDurations];
-[PLStateMetricsInput foregroundTimeSeconds];
-[PLStateMetricsInput hangDurations];
-[PLStateMetricsInput locationBestAccuracyNavSeconds];
-[PLStateMetricsInput locationBestAccuracySeconds];
-[PLStateMetricsInput locationHundredMetersSeconds];
-[PLStateMetricsInput locationKilometerSeconds];
-[PLStateMetricsInput locationReducedAccuracySeconds];
-[PLStateMetricsInput locationTenMetersSeconds];
-[PLStateMetricsInput locationThreeKilometersSeconds];
-[PLStateMetricsInput metalFrameRate];
-[PLStateMetricsInput scrollGlitches];
-[PLStateMetricsInput setActivationAfterPrewarmDurations:];
-[PLStateMetricsInput setActivationLaunchDurations:];
-[PLStateMetricsInput setBackgroundAudioTimeSeconds:];
-[PLStateMetricsInput setBackgroundExits:];
-[PLStateMetricsInput setBackgroundLaunchDurations:];
-[PLStateMetricsInput setBackgroundLocationTimeSeconds:];
-[PLStateMetricsInput setBackgroundTimeSeconds:];
-[PLStateMetricsInput setCellularConditionHistogram:];
-[PLStateMetricsInput setExtendedLaunchDurations:];
-[PLStateMetricsInput setForegroundExits:];
-[PLStateMetricsInput setForegroundLaunchDurations:];
-[PLStateMetricsInput setForegroundTimeSeconds:];
-[PLStateMetricsInput setHangDurations:];
-[PLStateMetricsInput setLocationBestAccuracyNavSeconds:];
-[PLStateMetricsInput setLocationHundredMetersSeconds:];
-[PLStateMetricsInput setLocationKilometerSeconds:];
-[PLStateMetricsInput setLocationReducedAccuracySeconds:];
-[PLStateMetricsInput setLocationTenMetersSeconds:];
-[PLStateMetricsInput setLocationThreeKilometersSeconds:];
-[PLStateMetricsInput setMetalFrameRate:];
-[PLStateMetricsInput setResumeDurations:];
-[PLStateMetricsInput setScrollGlitches:];
```
