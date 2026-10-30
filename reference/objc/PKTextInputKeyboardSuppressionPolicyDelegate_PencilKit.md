# `PKTextInputKeyboardSuppressionPolicyDelegate`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIKeyboardSuppressionPolicyDelegate`, `PKTextInputSupportedElementDelegate`
- 3 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _isQueryingLocaleIdentifier;
B _suppressLocaleIdentifier;
B isFloatingKeyboardVisible;
```

## Properties

```
@property (TB,N,V_suppressLocaleIdentifier) _suppressLocaleIdentifier;
@property (TB,N,VisFloatingKeyboardVisible) isFloatingKeyboardVisible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputKeyboardSuppressionPolicyDelegate isFloatingKeyboardVisible];
-[PKTextInputKeyboardSuppressionPolicyDelegate _recognitionLocaleIdentifier];
-[PKTextInputKeyboardSuppressionPolicyDelegate _shouldSuppressAssistantBarForDelegate:];
-[PKTextInputKeyboardSuppressionPolicyDelegate _shouldSuppressForDelegate:];
-[PKTextInputKeyboardSuppressionPolicyDelegate _suppressLocaleIdentifier];
-[PKTextInputKeyboardSuppressionPolicyDelegate set_suppressLocaleIdentifier:];
-[PKTextInputKeyboardSuppressionPolicyDelegate updateKeyboardSuppressionPolicy];
-[PKTextInputKeyboardSuppressionPolicyDelegate classesForKeyboardUISuppression];
-[PKTextInputKeyboardSuppressionPolicyDelegate _shouldSuppressKeyboardUIForDelegate:checkSource:];
-[PKTextInputKeyboardSuppressionPolicyDelegate isSupportedForTextInputTraits:];
-[PKTextInputKeyboardSuppressionPolicyDelegate setIsFloatingKeyboardVisible:];
```
