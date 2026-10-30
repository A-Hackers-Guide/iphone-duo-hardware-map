# `AVAnnotationRepresentation`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 1 properties, 13 instance methods, 4 class methods

## Instance variables

```
@"NSString" _representationType;
@"NSString" _version;
@"NSUUID" _identifier;
```

## Properties

```
@property (T@"NSUUID",C,N,V_identifier) identifier;
```

## Class methods

```
+[AVAnnotationRepresentation _annotationRepresentationWithPropertyList:binaryData:];
+[AVAnnotationRepresentation _createBindingDictionaryFromMetadataItemPayload:error:];
+[AVAnnotationRepresentation _createMetadataItemPayloadForData:identifier:error:];
+[AVAnnotationRepresentation _createMetadataItemPayloadForDataBinding:error:];
```

## Instance methods

```
-[AVAnnotationRepresentation identifier];
-[AVAnnotationRepresentation dealloc];
-[AVAnnotationRepresentation setIdentifier:];
-[AVAnnotationRepresentation hash];
-[AVAnnotationRepresentation _setVersion:];
-[AVAnnotationRepresentation _version];
-[AVAnnotationRepresentation copyWithZone:];
-[AVAnnotationRepresentation isEqual:];
-[AVAnnotationRepresentation _initWithPropertyList:binaryData:];
-[AVAnnotationRepresentation _initWithRepresentationType:];
-[AVAnnotationRepresentation _propertyListAndBinaryData:];
-[AVAnnotationRepresentation _representationType];
-[AVAnnotationRepresentation _setRepresentationType:];
```
