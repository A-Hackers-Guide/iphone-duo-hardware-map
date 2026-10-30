# `MTLSharedTextureHandle`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{MTLSharedTextureHandlePrivate=^{__IOSurface}@@} _priv;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
```

## Class methods

```
+[MTLSharedTextureHandle supportsSecureCoding];
```

## Instance methods

```
-[MTLSharedTextureHandle device];
-[MTLSharedTextureHandle label];
-[MTLSharedTextureHandle dealloc];
-[MTLSharedTextureHandle ioSurface];
-[MTLSharedTextureHandle encodeWithCoder:];
-[MTLSharedTextureHandle initWithCoder:];
-[MTLSharedTextureHandle initWithMachPort:];
-[MTLSharedTextureHandle createMachPort];
-[MTLSharedTextureHandle initWithIOSurface:label:];
```
