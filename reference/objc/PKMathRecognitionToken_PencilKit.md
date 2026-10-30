# `PKMathRecognitionToken`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _isTrigonometric;
@"NSUUID" _uuid;
@"PKMathRecognitionItem" _item;
q _type;
@"NSString" _text;
q _columnIndex;
@"NSArray" _errors;
@"NSArray" _alternatives;
@"NSArray" _renderableAlternatives;
{_NSRange="location"Q"length"Q} _characterRange;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (T@"PKMathRecognitionItem",W,N,V_item) item;
@property (Tq,N,V_type) type;
@property (T@"NSString",C,N,V_text) text;
@property (T{_NSRange=QQ},N,V_characterRange) characterRange;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_bounds) bounds;
@property (Tq,N,V_columnIndex) columnIndex;
@property (TB,N,V_isTrigonometric) isTrigonometric;
@property (T@"NSArray",C,N,V_errors) errors;
@property (T@"NSArray",C,N,V_alternatives) alternatives;
@property (T@"NSArray",C,N,V_renderableAlternatives) renderableAlternatives;
```

## Instance methods

```
-[PKMathRecognitionToken errors];
-[PKMathRecognitionToken setAlternatives:];
-[PKMathRecognitionToken setCharacterRange:];
-[PKMathRecognitionToken alternatives];
-[PKMathRecognitionToken debugDescription];
-[PKMathRecognitionToken setErrors:];
-[PKMathRecognitionToken text];
-[PKMathRecognitionToken uuid];
-[PKMathRecognitionToken init];
-[PKMathRecognitionToken setItem:];
-[PKMathRecognitionToken item];
-[PKMathRecognitionToken setBounds:];
-[PKMathRecognitionToken setType:];
-[PKMathRecognitionToken type];
-[PKMathRecognitionToken columnIndex];
-[PKMathRecognitionToken bounds];
-[PKMathRecognitionToken setText:];
-[PKMathRecognitionToken setColumnIndex:];
-[PKMathRecognitionToken characterRange];
-[PKMathRecognitionToken isTrigonometric];
-[PKMathRecognitionToken renderableAlternatives];
-[PKMathRecognitionToken setIsTrigonometric:];
-[PKMathRecognitionToken setRenderableAlternatives:];
```
