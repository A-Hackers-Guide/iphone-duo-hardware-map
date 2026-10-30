# `_UIVectorTextLayoutRun`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVectorTextLayoutRun`
- 9 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
Q _glyphCount;
@"NSAttributedString" _sourceString;
@"_UIVectorTextLayoutInfo" _layoutInfo;
Q _lineIndex;
^{__CTRun=} _runRef;
d _baseline;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lineRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _usedLineRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _usedRunRect;
```

## Properties

```
@property (T^{__CTRun=},R,N,V_runRef) _CTRun;
@property (Td,N,V_baseline) baseline;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_lineRect) lineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_usedLineRect) usedLineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_usedRunRect) usedRunRect;
@property (TQ,R,N,V_lineIndex) lineIndex;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIVectorTextLayoutRun renderInContext:];
-[_UIVectorTextLayoutRun dealloc];
-[_UIVectorTextLayoutRun string];
-[_UIVectorTextLayoutRun baseline];
-[_UIVectorTextLayoutRun glyphCount];
-[_UIVectorTextLayoutRun font];
-[_UIVectorTextLayoutRun setBaseline:];
-[_UIVectorTextLayoutRun setUsedRunRect:];
-[_UIVectorTextLayoutRun _CTRun];
-[_UIVectorTextLayoutRun _enumerateGlyphsUsingBlock:];
-[_UIVectorTextLayoutRun enumerateGlyphsUsingBlock:];
-[_UIVectorTextLayoutRun initWithCTRun:lineIndex:layoutInfo:];
-[_UIVectorTextLayoutRun lineIndex];
-[_UIVectorTextLayoutRun lineRect];
-[_UIVectorTextLayoutRun setLineRect:];
-[_UIVectorTextLayoutRun setUsedLineRect:];
-[_UIVectorTextLayoutRun shouldRender];
-[_UIVectorTextLayoutRun stringRange];
-[_UIVectorTextLayoutRun usedLineRect];
-[_UIVectorTextLayoutRun usedRunRect];
```
