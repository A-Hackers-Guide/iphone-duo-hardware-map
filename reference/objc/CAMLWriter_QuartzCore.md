# `CAMLWriter`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
^{_CAMLWriterPriv=^{__CFData}^{__CFURL}@^{_CAMLWriterElement}^{__CFString}^{__CFSet}^{__CFSet}ib1b1b1b1} _priv;
```

## Properties

```
@property (T@"NSURL",&) baseURL;
@property (T@"<CAMLWriterDelegate>",W) delegate;
```

## Class methods

```
+[CAMLWriter writerWithData:];
```

## Instance methods

```
-[CAMLWriter encodeObject:];
-[CAMLWriter baseURL];
-[CAMLWriter setBaseURL:];
-[CAMLWriter dealloc];
-[CAMLWriter setDelegate:];
-[CAMLWriter delegate];
-[CAMLWriter initWithData:];
-[CAMLWriter URLStringForResource:];
-[CAMLWriter _writeElementTree:];
-[CAMLWriter beginElement:];
-[CAMLWriter beginPropertyElement:];
-[CAMLWriter encodeObject:conditionally:];
-[CAMLWriter encodingForReverseSerializationTest];
-[CAMLWriter endElement];
-[CAMLWriter setElementAttribute:forKey:];
-[CAMLWriter setElementContent:];
-[CAMLWriter setEncodingForReverseSerializationTest:];
```
