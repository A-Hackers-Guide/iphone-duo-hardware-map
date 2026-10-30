# `PKManagedConfigurationState`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isPersonalizedHandwritingResultsAllowed;
B _isAutoCorrectionAllowed;
B _isSpellCheckAllowed;
B _isPredictiveKeyboardAllowed;
B _isImageWandAllowed;
B _isMathPaperSolvingAllowed;
B _isWritingToolsAllowed;
```

## Properties

```
@property (TB,R,N,V_isPersonalizedHandwritingResultsAllowed) isPersonalizedHandwritingResultsAllowed;
@property (TB,R,N,V_isAutoCorrectionAllowed) isAutoCorrectionAllowed;
@property (TB,R,N,V_isSpellCheckAllowed) isSpellCheckAllowed;
@property (TB,R,N,V_isPredictiveKeyboardAllowed) isPredictiveKeyboardAllowed;
@property (TB,R,N,V_isImageWandAllowed) isImageWandAllowed;
@property (TB,R,N,V_isMathPaperSolvingAllowed) isMathPaperSolvingAllowed;
@property (TB,R,N,V_isWritingToolsAllowed) isWritingToolsAllowed;
```

## Instance methods

```
-[PKManagedConfigurationState initFromDictionaryRepresentation:];
-[PKManagedConfigurationState isWritingToolsAllowed];
-[PKManagedConfigurationState isPredictiveKeyboardAllowed];
-[PKManagedConfigurationState isMathPaperSolvingAllowed];
-[PKManagedConfigurationState initWithDefaultValues];
-[PKManagedConfigurationState isImageWandAllowed];
-[PKManagedConfigurationState isAutoCorrectionAllowed];
-[PKManagedConfigurationState isSpellCheckAllowed];
-[PKManagedConfigurationState copyWithZone:];
-[PKManagedConfigurationState isEqual:];
-[PKManagedConfigurationState isPersonalizedHandwritingResultsAllowed];
-[PKManagedConfigurationState dictionaryRepresentation];
-[PKManagedConfigurationState initFromCFPreferences];
-[PKManagedConfigurationState initFromProfileConnection:];
```
