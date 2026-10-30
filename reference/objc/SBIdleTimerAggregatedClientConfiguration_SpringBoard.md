# `SBIdleTimerAggregatedClientConfiguration`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBIdleTimerTimeoutRange" _resolvedExpirationTimeoutRange;
@"SBIdleTimerConfigurationDisablesTimerSetting" _disableTimerSetting;
@"SBIdleTimerTimeoutPrecedenceSettings" _minExpirationTimeoutSettings;
@"SBIdleTimerTimeoutPrecedenceSettings" _maxExpirationTimeoutSettings;
```

## Properties

```
@property (T@"SBIdleTimerConfigurationDisablesTimerSetting",R,N,V_disableTimerSetting) disableTimerSetting;
@property (T@"SBIdleTimerTimeoutPrecedenceSettings",R,N,V_minExpirationTimeoutSettings) minExpirationTimeoutSettings;
@property (T@"SBIdleTimerTimeoutPrecedenceSettings",R,N,V_maxExpirationTimeoutSettings) maxExpirationTimeoutSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerAggregatedClientConfiguration succinctDescriptionBuilder];
-[SBIdleTimerAggregatedClientConfiguration descriptionWithMultilinePrefix:];
-[SBIdleTimerAggregatedClientConfiguration succinctDescription];
-[SBIdleTimerAggregatedClientConfiguration description];
-[SBIdleTimerAggregatedClientConfiguration descriptionBuilderWithMultilinePrefix:];
-[SBIdleTimerAggregatedClientConfiguration setDisablesTimerWithPrecedence:];
-[SBIdleTimerAggregatedClientConfiguration disableTimerSetting];
-[SBIdleTimerAggregatedClientConfiguration expirationTimeoutIntervalRangeForPrecedence:];
-[SBIdleTimerAggregatedClientConfiguration maxExpirationTimeoutSettings];
-[SBIdleTimerAggregatedClientConfiguration minExpirationTimeoutSettings];
-[SBIdleTimerAggregatedClientConfiguration resolvedExpirationTimeoutRange];
-[SBIdleTimerAggregatedClientConfiguration setMaxExpirationTimeout:ifLeastForPrecedence:];
-[SBIdleTimerAggregatedClientConfiguration setMaxExpirationTimeout:withPrecedence:];
-[SBIdleTimerAggregatedClientConfiguration setMinExpirationTimeout:ifGreatestForPrecedence:];
-[SBIdleTimerAggregatedClientConfiguration setMinExpirationTimeout:withPrecedence:];
```
