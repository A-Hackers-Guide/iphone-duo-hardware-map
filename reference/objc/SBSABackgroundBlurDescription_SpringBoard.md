# `SBSABackgroundBlurDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAInterfaceElementIdentifying`, `SBSABackgroundBlurDescribing`, `NSCopying`, `SBSABlockMutating`
- 4 instance variables, 9 properties, 19 instance methods, 3 class methods

## Instance variables

```
B _blurHidden;
d _blurElementCornerRadius;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _blurFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _blurElementFrame;
```

## Properties

```
@property (TB,N,GisBlurHidden,S_setBlurHidden:,V_blurHidden) blurHidden;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setBlurFrame:,V_blurFrame) blurFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setBlurElementFrame:,V_blurElementFrame) blurElementFrame;
@property (Td,N,S_setBlurElementCornerRadius:,V_blurElementCornerRadius) blurElementCornerRadius;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSUUID",R,C,N) interfaceElementIdentifier;
```

## Class methods

```
+[SBSABackgroundBlurDescription initialize];
+[SBSABackgroundBlurDescription instanceWithBlock:];
+[SBSABackgroundBlurDescription mutatorClass];
```

## Instance methods

```
-[SBSABackgroundBlurDescription interfaceElementIdentifier];
-[SBSABackgroundBlurDescription hash];
-[SBSABackgroundBlurDescription description];
-[SBSABackgroundBlurDescription copyWithZone:];
-[SBSABackgroundBlurDescription isEqual:];
-[SBSABackgroundBlurDescription copyWithBlock:];
-[SBSABackgroundBlurDescription membersForCoder];
-[SBSABackgroundBlurDescription isBlurHidden];
-[SBSABackgroundBlurDescription _setBlurHidden:];
-[SBSABackgroundBlurDescription _setBlurElementCornerRadius:];
-[SBSABackgroundBlurDescription _setBlurElementFrame:];
-[SBSABackgroundBlurDescription _setBlurFrame:];
-[SBSABackgroundBlurDescription blurElementCornerRadius];
-[SBSABackgroundBlurDescription blurElementFrame];
-[SBSABackgroundBlurDescription blurFrame];
-[SBSABackgroundBlurDescription copyBySettingBlurElementCornerRadius:];
-[SBSABackgroundBlurDescription copyBySettingBlurElementFrame:];
-[SBSABackgroundBlurDescription copyBySettingBlurFrame:];
-[SBSABackgroundBlurDescription copyBySettingBlurHidden:];
```
