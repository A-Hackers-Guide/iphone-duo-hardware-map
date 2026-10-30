# `MTLSharedEventHandle`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
^{MTLSharedEventHandlePrivate=I@Q} _priv;
```

## Properties

```
@property (T@"NSString",R) label;
```

## Class methods

```
+[MTLSharedEventHandle supportsSecureCoding];
```

## Instance methods

```
-[MTLSharedEventHandle label];
-[MTLSharedEventHandle dealloc];
-[MTLSharedEventHandle encodeWithCoder:];
-[MTLSharedEventHandle initWithCoder:];
-[MTLSharedEventHandle eventPort];
-[MTLSharedEventHandle initWithSharedEvent:];
-[MTLSharedEventHandle labelTraceID];
```
