# `PKExternalElement`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBox;
@ _identifier;
^{CGPath=} _path;
```

## Properties

```
@property (T@,R,N,V_identifier) identifier;
@property (T^{CGPath=},R,N,V_path) path;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) boundingBox;
```

## Instance methods

```
-[PKExternalElement identifier];
-[PKExternalElement dealloc];
-[PKExternalElement boundingBox];
-[PKExternalElement hash];
-[PKExternalElement isEqual:];
-[PKExternalElement path];
-[PKExternalElement initWithIdentifier:path:];
```
