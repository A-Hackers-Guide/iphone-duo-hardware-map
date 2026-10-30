# `AAAccessoryFeatureFlagRules`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _rulesByFeatureID;
```

## Class methods

```
+[AAAccessoryFeatureFlagRules defaultRules];
```

## Instance methods

```
-[AAAccessoryFeatureFlagRules init];
-[AAAccessoryFeatureFlagRules addRuleForFeatureID:stateDeterminer:];
-[AAAccessoryFeatureFlagRules addRuleForFeatureID:stateDeterminer:payloadGenerator:];
-[AAAccessoryFeatureFlagRules applyRulesToAccessory:];
```
