# `_UIWTCProofreadingSuggestionInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _identifier;
@"NSUUID" _contextID;
@"NSAttributedString" _attributedString;
q _lengthDelta;
q _state;
@"NSArray" _singleContainerSubrangesOfAdjustedOriginalRange;
@"_UIWTCProofreadingDecorationInfo" _underlineInfo;
@"_UIWTCProofreadingDecorationInfo" _highlightInfo;
{_NSRange="location"Q"length"Q} _originalRange;
```

## Properties

```
@property (T@"NSUUID",R,N,V_identifier) identifier;
@property (T@"NSUUID",R,N,V_contextID) contextID;
@property (T@"NSAttributedString",R,N,V_attributedString) attributedString;
@property (T{_NSRange=QQ},R,N,V_originalRange) originalRange;
@property (Tq,R,N,V_lengthDelta) lengthDelta;
@property (Tq,R,N,V_state) state;
@property (T@"NSArray",C,N,V_singleContainerSubrangesOfAdjustedOriginalRange) singleContainerSubrangesOfAdjustedOriginalRange;
@property (T@"_UIWTCProofreadingDecorationInfo",&,N,V_underlineInfo) underlineInfo;
@property (T@"_UIWTCProofreadingDecorationInfo",&,N,V_highlightInfo) highlightInfo;
```

## Instance methods

```
-[_UIWTCProofreadingSuggestionInfo identifier];
-[_UIWTCProofreadingSuggestionInfo attributedString];
-[_UIWTCProofreadingSuggestionInfo description];
-[_UIWTCProofreadingSuggestionInfo contextID];
-[_UIWTCProofreadingSuggestionInfo state];
-[_UIWTCProofreadingSuggestionInfo decorationContainerForSubrange:];
-[_UIWTCProofreadingSuggestionInfo highlightInfo];
-[_UIWTCProofreadingSuggestionInfo initWithProofreadingSuggestionInfo:state:];
-[_UIWTCProofreadingSuggestionInfo initWithWTTextSuggestion:withOffset:inAttributedString:contextID:];
-[_UIWTCProofreadingSuggestionInfo lengthDelta];
-[_UIWTCProofreadingSuggestionInfo originalRange];
-[_UIWTCProofreadingSuggestionInfo setHighlightInfo:];
-[_UIWTCProofreadingSuggestionInfo setSingleContainerSubrangesOfAdjustedOriginalRange:];
-[_UIWTCProofreadingSuggestionInfo setUnderlineInfo:];
-[_UIWTCProofreadingSuggestionInfo singleContainerSubrangesOfAdjustedOriginalRange];
-[_UIWTCProofreadingSuggestionInfo underlineInfo];
```
