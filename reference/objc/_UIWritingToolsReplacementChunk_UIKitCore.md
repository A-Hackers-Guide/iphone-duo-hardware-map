# `_UIWritingToolsReplacementChunk`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _uuid;
@"NSAttributedString" _replacement;
q _lengthDelta;
q _originalEndIndex;
{_NSRange="location"Q"length"Q} _originalRange;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (T{_NSRange=QQ},R,N,V_originalRange) originalRange;
@property (T@"NSAttributedString",R,C,N,V_replacement) replacement;
@property (Tq,R,N,V_lengthDelta) lengthDelta;
@property (Tq,R,N,V_originalEndIndex) originalEndIndex;
```

## Instance methods

```
-[_UIWritingToolsReplacementChunk uuid];
-[_UIWritingToolsReplacementChunk description];
-[_UIWritingToolsReplacementChunk initWithReplacementChunk:originalRange:uuid:];
-[_UIWritingToolsReplacementChunk lengthDelta];
-[_UIWritingToolsReplacementChunk originalEndIndex];
-[_UIWritingToolsReplacementChunk originalRange];
-[_UIWritingToolsReplacementChunk replacement];
```
