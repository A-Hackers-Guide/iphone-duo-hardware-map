# `_UIStatesFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorConfiguration`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _stateChangeConfigurations;
@"NSString" _initialState;
```

## Properties

```
@property (T@"NSString",&,N,V_initialState) initialState;
@property (T@"NSDictionary",&,N,V_stateChangeConfigurations) stateChangeConfigurations;
```

## Class methods

```
+[_UIStatesFeedbackGeneratorConfiguration keyFromState:toState:];
```

## Instance methods

```
-[_UIStatesFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIStatesFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_UIStatesFeedbackGeneratorConfiguration setInitialState:];
-[_UIStatesFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
-[_UIStatesFeedbackGeneratorConfiguration initialState];
-[_UIStatesFeedbackGeneratorConfiguration copyWithZone:];
-[_UIStatesFeedbackGeneratorConfiguration setStateChangeConfigurations:];
-[_UIStatesFeedbackGeneratorConfiguration stateChangeConfigurations];
```
