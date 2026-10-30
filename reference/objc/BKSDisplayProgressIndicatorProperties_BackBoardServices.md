# `BKSDisplayProgressIndicatorProperties`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionProviding`
- 2 instance variables, 6 properties, 12 instance methods, 2 class methods

## Instance variables

```
q _style;
{CGPoint="x"d"y"d} _position;
```

## Properties

```
@property (Tq,R,N,V_style) style;
@property (T{CGPoint=dd},R,N,V_position) position;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSDisplayProgressIndicatorProperties supportsSecureCoding];
+[BKSDisplayProgressIndicatorProperties progressIndicatorWithStyle:position:];
```

## Instance methods

```
-[BKSDisplayProgressIndicatorProperties position];
-[BKSDisplayProgressIndicatorProperties succinctDescriptionBuilder];
-[BKSDisplayProgressIndicatorProperties descriptionWithMultilinePrefix:];
-[BKSDisplayProgressIndicatorProperties style];
-[BKSDisplayProgressIndicatorProperties succinctDescription];
-[BKSDisplayProgressIndicatorProperties encodeWithCoder:];
-[BKSDisplayProgressIndicatorProperties hash];
-[BKSDisplayProgressIndicatorProperties description];
-[BKSDisplayProgressIndicatorProperties initWithCoder:];
-[BKSDisplayProgressIndicatorProperties isEqual:];
-[BKSDisplayProgressIndicatorProperties descriptionBuilderWithMultilinePrefix:];
-[BKSDisplayProgressIndicatorProperties _initWithStyle:position:];
```
