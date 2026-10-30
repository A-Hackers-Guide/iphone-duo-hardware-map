# `BKSTouchAnnotation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionProviding`
- 3 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
I _touchIdentifier;
@"NSString" _text;
@"NSString" _uniqueIdentifier;
```

## Properties

```
@property (TI,N,V_touchIdentifier) touchIdentifier;
@property (T@"NSString",C,N,V_text) text;
@property (T@"NSString",C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSTouchAnnotation supportsSecureCoding];
```

## Instance methods

```
-[BKSTouchAnnotation touchIdentifier];
-[BKSTouchAnnotation text];
-[BKSTouchAnnotation succinctDescriptionBuilder];
-[BKSTouchAnnotation setTouchIdentifier:];
-[BKSTouchAnnotation setUniqueIdentifier:];
-[BKSTouchAnnotation descriptionWithMultilinePrefix:];
-[BKSTouchAnnotation uniqueIdentifier];
-[BKSTouchAnnotation succinctDescription];
-[BKSTouchAnnotation encodeWithCoder:];
-[BKSTouchAnnotation initWithCoder:];
-[BKSTouchAnnotation setText:];
-[BKSTouchAnnotation descriptionBuilderWithMultilinePrefix:];
```
