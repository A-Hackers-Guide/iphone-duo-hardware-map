# `UIKeyboardCandidateViewState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `TUICandidateViewState`
- 15 instance variables, 19 properties, 32 instance methods, 1 class methods

## Instance variables

```
B _hasBackdrop;
B _candidateNumberEnabled;
@"UIKeyboardCandidateViewStyle" _style;
@"UIKeyboardCandidateViewStyle" _disambiguationStyle;
q _primaryGridRowType;
q _disambiguationGridRowType;
q _disambiguationGridPosition;
q _sortControlPosition;
q _inlineTextViewPosition;
q _arrowButtonPosition;
q _arrowButtonDirection;
d _yOffset;
d _additionalHeight;
Q _borders;
{CGPoint="x"d"y"d} _arrowButtonOffset;
```

## Properties

```
@property (T@"UIKeyboardCandidateViewStyle",&,N,V_style) style;
@property (T@"UIKeyboardCandidateViewStyle",&,N,V_disambiguationStyle) disambiguationStyle;
@property (Tq,N,V_primaryGridRowType) primaryGridRowType;
@property (Tq,N,V_disambiguationGridRowType) disambiguationGridRowType;
@property (Tq,N,V_disambiguationGridPosition) disambiguationGridPosition;
@property (Tq,N,V_sortControlPosition) sortControlPosition;
@property (Tq,N,V_inlineTextViewPosition) inlineTextViewPosition;
@property (Tq,N,V_arrowButtonPosition) arrowButtonPosition;
@property (Tq,N,V_arrowButtonDirection) arrowButtonDirection;
@property (TB,N,V_hasBackdrop) hasBackdrop;
@property (TB,N,V_candidateNumberEnabled) candidateNumberEnabled;
@property (Td,N,V_yOffset) yOffset;
@property (Td,N,V_additionalHeight) additionalHeight;
@property (T{CGPoint=dd},N,V_arrowButtonOffset) arrowButtonOffset;
@property (TQ,N,V_borders) borders;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardCandidateViewState resolveInstanceMethod:];
```

## Instance methods

```
-[UIKeyboardCandidateViewState style];
-[UIKeyboardCandidateViewState yOffset];
-[UIKeyboardCandidateViewState setStyle:];
-[UIKeyboardCandidateViewState copyWithZone:];
-[UIKeyboardCandidateViewState isEqual:];
-[UIKeyboardCandidateViewState borders];
-[UIKeyboardCandidateViewState setHasBackdrop:];
-[UIKeyboardCandidateViewState additionalHeight];
-[UIKeyboardCandidateViewState arrowButtonDirection];
-[UIKeyboardCandidateViewState arrowButtonOffset];
-[UIKeyboardCandidateViewState arrowButtonPosition];
-[UIKeyboardCandidateViewState candidateNumberEnabled];
-[UIKeyboardCandidateViewState disambiguationGridPosition];
-[UIKeyboardCandidateViewState disambiguationGridRowType];
-[UIKeyboardCandidateViewState disambiguationStyle];
-[UIKeyboardCandidateViewState hasBackdrop];
-[UIKeyboardCandidateViewState inlineTextViewPosition];
-[UIKeyboardCandidateViewState primaryGridRowType];
-[UIKeyboardCandidateViewState setAdditionalHeight:];
-[UIKeyboardCandidateViewState setArrowButtonDirection:];
-[UIKeyboardCandidateViewState setArrowButtonOffset:];
-[UIKeyboardCandidateViewState setArrowButtonPosition:];
-[UIKeyboardCandidateViewState setBorders:];
-[UIKeyboardCandidateViewState setCandidateNumberEnabled:];
-[UIKeyboardCandidateViewState setDisambiguationGridPosition:];
-[UIKeyboardCandidateViewState setDisambiguationGridRowType:];
-[UIKeyboardCandidateViewState setDisambiguationStyle:];
-[UIKeyboardCandidateViewState setInlineTextViewPosition:];
-[UIKeyboardCandidateViewState setPrimaryGridRowType:];
-[UIKeyboardCandidateViewState setSortControlPosition:];
-[UIKeyboardCandidateViewState setYOffset:];
-[UIKeyboardCandidateViewState sortControlPosition];
```
