# `UIItemProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSItemProvider`
- 1 instance variables, 5 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _teamMetadata;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_teamMetadata) teamMetadata;
@property (T{CGSize=dd},N) estimatedDisplayedSize;
@property (T@"NSString",C,N) name;
@property (T@"NSDate",C,N) modificationDate;
@property (T@"NSNumber",C,N) size;
```

## Instance methods

```
-[UIItemProvider setModificationDate:];
-[UIItemProvider modificationDate];
-[UIItemProvider canInstantiateObjectOfClass:];
-[UIItemProvider size];
-[UIItemProvider setName:];
-[UIItemProvider name];
-[UIItemProvider setSize:];
-[UIItemProvider _availableTypes];
-[UIItemProvider _objectOfClass:data:typeIdentifier:error:];
-[UIItemProvider _readableTypeIdentifiersForItemProviderForClass:];
-[UIItemProvider canLoadObjectOfClass:];
-[UIItemProvider loadObjectOfClass:completionHandler:];
-[UIItemProvider initWithPBItem:];
-[UIItemProvider canCreateObjectOfClass:];
-[UIItemProvider copyDataRepresentationForTypeIdentifier:completionBlock:];
-[UIItemProvider copyDataRepresentationForTypeIdentifier:error:];
-[UIItemProvider copyDataRepresentationForTypeIdentifier:options:completionBlock:];
-[UIItemProvider copyDataRepresentationForTypeIdentifier:options:error:];
-[UIItemProvider copyFileRepresentationForTypeIdentifier:completionBlock:];
-[UIItemProvider copyFileRepresentationForTypeIdentifier:error:];
-[UIItemProvider copyFileRepresentationForTypeIdentifier:toURL:options:completionBlock:];
-[UIItemProvider copyFileRepresentationForTypeIdentifier:toURL:options:error:];
-[UIItemProvider createObjectOfClass:completionBlock:];
-[UIItemProvider createObjectOfClass:error:];
-[UIItemProvider estimatedDisplayedSize];
-[UIItemProvider getInPlaceFileRepresentationForTypeIdentifier:completionBlock:];
-[UIItemProvider getInPlaceFileRepresentationForTypeIdentifier:inPlace:error:];
-[UIItemProvider getInPlaceFileRepresentationForTypeIdentifier:options:completionBlock:];
-[UIItemProvider getInPlaceFileRepresentationForTypeIdentifier:options:error:];
-[UIItemProvider initWithPBItem:loadRequestContext:];
-[UIItemProvider initWithPBItem:loadRequestContext:secureRetryHandler:];
-[UIItemProvider instantiateObjectOfClass:options:completionBlock:];
-[UIItemProvider instantiateObjectOfClass:options:error:];
-[UIItemProvider registerDataRepresentationForTypeIdentifier:loadHandler:];
-[UIItemProvider registerDataRepresentationForTypeIdentifier:options:loadHandler:];
-[UIItemProvider registerFileRepresentationForTypeIdentifier:fileOptions:loadHandler:];
-[UIItemProvider registerFileRepresentationForTypeIdentifier:fileOptions:options:loadHandler:];
-[UIItemProvider registerObject:options:];
-[UIItemProvider registerObjectOfClass:options:loadHandler:];
-[UIItemProvider setEstimatedDisplayedSize:];
-[UIItemProvider setTeamMetadata:];
-[UIItemProvider teamMetadata];
```
