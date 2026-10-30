# `MTLMessageFilter`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"<MTLDevice>" _device;
Q _messageType;
```

## Properties

```
@property (T@"<MTLDevice>",R,&,V_device) device;
@property (TQ,R,V_messageType) messageType;
```

## Class methods

```
+[MTLMessageFilter filter:device:];
```

## Instance methods

```
-[MTLMessageFilter setDevice:];
-[MTLMessageFilter device];
-[MTLMessageFilter messageType];
-[MTLMessageFilter init:device:];
```
