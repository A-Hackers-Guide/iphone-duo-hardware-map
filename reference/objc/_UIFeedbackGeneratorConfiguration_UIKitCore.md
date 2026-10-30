# `_UIFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 12 instance variables, 16 properties, 41 instance methods, 5 class methods

## Instance variables

```
B _settingsEnabled;
B _setup;
B _enabled;
@"NSSet" _usedFeedbacks;
@? _preparationBlock;
# _clientClass;
@"NSString" _usage;
q _requiredSupportLevel;
q _requiredPeripheralSupportLevel;
q _activationStyle;
q _outputMode;
@"NSString" __stats_key;
```

## Properties

```
@property (T@?,C,N,V_preparationBlock) preparationBlock;
@property (T#,C,N,V_clientClass) clientClass;
@property (T@"NSString",C,N,V_usage) usage;
@property (Tq,N,V_requiredSupportLevel) requiredSupportLevel;
@property (Tq,N,V_requiredPeripheralSupportLevel) requiredPeripheralSupportLevel;
@property (Tq,N,V_activationStyle) activationStyle;
@property (Tq,N,V_outputMode) outputMode;
@property (TB,R,N) defaultEnabled;
@property (TB,N,V_settingsEnabled) settingsEnabled;
@property (TB,N,GisSetup,V_setup) setup;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"NSArray",R,N) feedbackKeyPaths;
@property (T@"NSSet",R,N,V_usedFeedbacks) usedFeedbacks;
@property (T@"NSString",R,N) descriptionKey;
@property (T@"NSArray",R,N) hidFeedbackPatternNameKeyPaths;
@property (T@"NSString",C,N,V__stats_key) _stats_key;
```

## Class methods

```
+[_UIFeedbackGeneratorConfiguration defaultConfiguration];
+[_UIFeedbackGeneratorConfiguration _configurationWithKey:preparationBlock:];
+[_UIFeedbackGeneratorConfiguration _configurationWithKey:requiredSupportLevel:preparationBlock:];
+[_UIFeedbackGeneratorConfiguration _disabledConfiguration];
+[_UIFeedbackGeneratorConfiguration _enableHIDFeedbackForAllGenerators];
```

## Instance methods

```
-[_UIFeedbackGeneratorConfiguration usage];
-[_UIFeedbackGeneratorConfiguration _stats_key];
-[_UIFeedbackGeneratorConfiguration init];
-[_UIFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIFeedbackGeneratorConfiguration requiredPeripheralSupportLevel];
-[_UIFeedbackGeneratorConfiguration dealloc];
-[_UIFeedbackGeneratorConfiguration _updateEnabled];
-[_UIFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_UIFeedbackGeneratorConfiguration _setupIfNecessary];
-[_UIFeedbackGeneratorConfiguration clientClass];
-[_UIFeedbackGeneratorConfiguration defaultEnabled];
-[_UIFeedbackGeneratorConfiguration isEnabled];
-[_UIFeedbackGeneratorConfiguration setEnabled:];
-[_UIFeedbackGeneratorConfiguration description];
-[_UIFeedbackGeneratorConfiguration isSetup];
-[_UIFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
-[_UIFeedbackGeneratorConfiguration setUsage:];
-[_UIFeedbackGeneratorConfiguration requiredSupportLevel];
-[_UIFeedbackGeneratorConfiguration copyWithZone:];
-[_UIFeedbackGeneratorConfiguration isEqual:];
-[_UIFeedbackGeneratorConfiguration activationStyle];
-[_UIFeedbackGeneratorConfiguration setClientClass:];
-[_UIFeedbackGeneratorConfiguration settingsEnabled];
-[_UIFeedbackGeneratorConfiguration _preferencesUpdated:];
-[_UIFeedbackGeneratorConfiguration _shouldEnable];
-[_UIFeedbackGeneratorConfiguration _updateFeedbackForOutputMode:];
-[_UIFeedbackGeneratorConfiguration _updateFeedbacksForOutputMode:];
-[_UIFeedbackGeneratorConfiguration descriptionKey];
-[_UIFeedbackGeneratorConfiguration outputMode];
-[_UIFeedbackGeneratorConfiguration preparationBlock];
-[_UIFeedbackGeneratorConfiguration setActivationStyle:];
-[_UIFeedbackGeneratorConfiguration setOutputMode:];
-[_UIFeedbackGeneratorConfiguration setPreparationBlock:];
-[_UIFeedbackGeneratorConfiguration setRequiredPeripheralSupportLevel:];
-[_UIFeedbackGeneratorConfiguration setRequiredSupportLevel:];
-[_UIFeedbackGeneratorConfiguration setSettingsEnabled:];
-[_UIFeedbackGeneratorConfiguration setSetup:];
-[_UIFeedbackGeneratorConfiguration set_stats_key:];
-[_UIFeedbackGeneratorConfiguration tweakedConfigurationForCaller:usage:];
-[_UIFeedbackGeneratorConfiguration tweakedConfigurationForClass:usage:];
-[_UIFeedbackGeneratorConfiguration usedFeedbacks];
```
