# `CAMLParser`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 21 instance methods, 2 class methods

## Instance variables

```
^{_CAMLParserData=} _data;
```

## Properties

```
@property (T@"NSURL",&) baseURL;
@property (T@"<CAMLParserDelegate>",W) delegate;
@property (T@"NSError",R) error;
@property (T@,R) result;
```

## Class methods

```
+[CAMLParser parseContentsOfURL:];
+[CAMLParser parser];
```

## Instance methods

```
-[CAMLParser baseURL];
-[CAMLParser didLoadResource:fromURL:];
-[CAMLParser setBaseURL:];
-[CAMLParser willLoadResourceFromURL:];
-[CAMLParser setElementValue:];
-[CAMLParser objectById:];
-[CAMLParser init];
-[CAMLParser parseBytes:length:];
-[CAMLParser dealloc];
-[CAMLParser elementValue];
-[CAMLParser parseString:];
-[CAMLParser parserError:];
-[CAMLParser error];
-[CAMLParser setDelegate:];
-[CAMLParser result];
-[CAMLParser parseData:];
-[CAMLParser parseContentsOfURL:];
-[CAMLParser delegate];
-[CAMLParser parserWarning:];
-[CAMLParser attributeForKey:remove:];
-[CAMLParser didFailToLoadResourceFromURL:];
```
