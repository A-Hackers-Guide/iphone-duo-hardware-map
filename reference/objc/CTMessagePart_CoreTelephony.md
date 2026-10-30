# `CTMessagePart`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSString" _contentType;
@"NSMutableDictionary" _contentTypeParams;
@"NSString" _contentId;
@"NSString" _contentLocation;
@"NSData" _data;
```

## Properties

```
@property (T@"NSString",C,N,V_contentType) contentType;
@property (T@"NSString",C,N,V_contentId) contentId;
@property (T@"NSString",C,N,V_contentLocation) contentLocation;
@property (T@"NSData",C,N,V_data) data;
```

## Instance methods

```
-[CTMessagePart setContentType:];
-[CTMessagePart contentType];
-[CTMessagePart data];
-[CTMessagePart setData:];
-[CTMessagePart contentId];
-[CTMessagePart setContentId:];
-[CTMessagePart initWithData:contentType:];
-[CTMessagePart contentLocation];
-[CTMessagePart addContentTypeParameterWithName:value:];
-[CTMessagePart allContentTypeParameterNames];
-[CTMessagePart contentTypeParameterWithName:];
-[CTMessagePart setContentLocation:];
```
