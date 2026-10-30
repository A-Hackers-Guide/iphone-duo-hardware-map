# `EspressoFaceDetectedObject`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ExternalDetectedObject`
- 4 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
f confidence;
q objectType;
{CGPoint="x"d"y"d} center;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} bounds;
```

## Properties

```
@property (Tf,Vconfidence) confidence;
@property (Tq,VobjectType) objectType;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},Vbounds) bounds;
@property (T{CGPoint=dd},Vcenter) center;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[EspressoFaceDetectedObject objectType];
-[EspressoFaceDetectedObject setCenter:];
-[EspressoFaceDetectedObject setBounds:];
-[EspressoFaceDetectedObject setConfidence:];
-[EspressoFaceDetectedObject center];
-[EspressoFaceDetectedObject bounds];
-[EspressoFaceDetectedObject confidence];
-[EspressoFaceDetectedObject setObjectType:];
-[EspressoFaceDetectedObject initWithOptionsXloc:yloc:size:confidence:];
```
