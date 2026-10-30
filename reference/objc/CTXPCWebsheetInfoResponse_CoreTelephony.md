# `CTXPCWebsheetInfoResponse`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCResponseMessage`
- 0 instance variables, 4 properties, 8 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",R,N) urlString;
@property (T@"NSURL",R,N) url;
@property (T@"NSDictionary",R,N) postdata;
@property (T@"NSString",R,N) type;
```

## Class methods

```
+[CTXPCWebsheetInfoResponse allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCWebsheetInfoResponse urlString];
-[CTXPCWebsheetInfoResponse ct_shortName];
-[CTXPCWebsheetInfoResponse type];
-[CTXPCWebsheetInfoResponse url];
-[CTXPCWebsheetInfoResponse initWithURL:postdata:];
-[CTXPCWebsheetInfoResponse initWithURLString:postdata:];
-[CTXPCWebsheetInfoResponse initWithURLString:postdata:type:];
-[CTXPCWebsheetInfoResponse postdata];
```
