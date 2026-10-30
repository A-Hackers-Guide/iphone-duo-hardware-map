# `_UITextSelectionSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISettings`
- 12 instance variables, 12 properties, 25 instance methods, 1 class methods

## Instance variables

```
d _minPinkWidth;
d _maxPinkWidth;
d _pinkWidthFactor;
d _linear;
d _parabolic;
d _gain;
d _allowableSeparation;
d _allowableForceMovement;
@"NSNumber" _shouldUseAcceleration;
@"NSNumber" _shouldPreferEndOfWord;
@"NSNumber" _allowExtendingSelections;
@"NSNumber" _enableDeepPress;
```

## Properties

```
@property (Td,N,V_minPinkWidth) minPinkWidth;
@property (Td,N,V_maxPinkWidth) maxPinkWidth;
@property (Td,N,V_pinkWidthFactor) pinkWidthFactor;
@property (Td,N,V_linear) linear;
@property (Td,N,V_parabolic) parabolic;
@property (Td,N,V_gain) gain;
@property (Td,N,V_allowableSeparation) allowableSeparation;
@property (Td,N,V_allowableForceMovement) allowableForceMovement;
@property (T@"NSNumber",&,N,V_shouldUseAcceleration) shouldUseAcceleration;
@property (T@"NSNumber",&,N,V_shouldPreferEndOfWord) shouldPreferEndOfWord;
@property (T@"NSNumber",&,N,V_allowExtendingSelections) allowExtendingSelections;
@property (T@"NSNumber",&,N,V_enableDeepPress) enableDeepPress;
```

## Class methods

```
+[_UITextSelectionSettings sharedInstance];
```

## Instance methods

```
-[_UITextSelectionSettings gain];
-[_UITextSelectionSettings shouldPreferEndOfWord];
-[_UITextSelectionSettings parabolic];
-[_UITextSelectionSettings setEnableDeepPress:];
-[_UITextSelectionSettings maxPinkWidth];
-[_UITextSelectionSettings setParabolic:];
-[_UITextSelectionSettings setAllowExtendingSelections:];
-[_UITextSelectionSettings setLinear:];
-[_UITextSelectionSettings setMaxPinkWidth:];
-[_UITextSelectionSettings setAllowableForceMovement:];
-[_UITextSelectionSettings shouldUseAcceleration];
-[_UITextSelectionSettings setPinkWidthFactor:];
-[_UITextSelectionSettings enableDeepPress];
-[_UITextSelectionSettings allowableSeparation];
-[_UITextSelectionSettings setDefaultValues];
-[_UITextSelectionSettings linear];
-[_UITextSelectionSettings setShouldUseAcceleration:];
-[_UITextSelectionSettings pinkWidthFactor];
-[_UITextSelectionSettings setShouldPreferEndOfWord:];
-[_UITextSelectionSettings allowableForceMovement];
-[_UITextSelectionSettings allowExtendingSelections];
-[_UITextSelectionSettings setGain:];
-[_UITextSelectionSettings setAllowableSeparation:];
-[_UITextSelectionSettings setMinPinkWidth:];
-[_UITextSelectionSettings minPinkWidth];
```
