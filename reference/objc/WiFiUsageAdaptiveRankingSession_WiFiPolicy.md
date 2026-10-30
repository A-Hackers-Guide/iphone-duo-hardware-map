# `WiFiUsageAdaptiveRankingSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageSession`
- 3 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
{?="wifiRSSI"i"lqaScore"C"cellScore"I"band"C"icEnabled"B"cellularFallbackEnabled"B"bssEnvironment"@"NSString""firstValidLQAScore"C"timeToFirstValidLQASec"I"firstValidRSSI"i"firstValidBand"C} _startSnapshot;
{?="wifiRSSI"i"lqaScore"C"cellScore"I"band"C"icEnabled"B"cellularFallbackEnabled"B"bssEnvironment"@"NSString""firstValidLQAScore"C"timeToFirstValidLQASec"I"firstValidRSSI"i"firstValidBand"C} _endSnapshot;
@"NSString" _endReason;
```

## Instance methods

```
-[WiFiUsageAdaptiveRankingSession metricName];
-[WiFiUsageAdaptiveRankingSession sessionDidStartWithSnapshot:];
-[WiFiUsageAdaptiveRankingSession eventDictionary:];
-[WiFiUsageAdaptiveRankingSession initWithInterfaceName:andCapabilities:];
-[WiFiUsageAdaptiveRankingSession sessionDidEndWithReason:snapshot:];
-[WiFiUsageAdaptiveRankingSession copyWithZone:];
```
