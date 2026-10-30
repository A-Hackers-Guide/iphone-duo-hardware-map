# `DCActivityItemSource`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIActivityItemSourceAttachment`, `UIActivityItemSource`
- 1 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"ICDocCamDocumentInfoCollection" _docInfoCollection;
```

## Properties

```
@property (T@"ICDocCamDocumentInfoCollection",W,N,V_docInfoCollection) docInfoCollection;
@property (T@"NSString",R,C,N) attachmentTypeUTI;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DCActivityItemSource activityViewController:dataTypeIdentifierForActivityType:];
-[DCActivityItemSource activityViewControllerPlaceholderItem:];
-[DCActivityItemSource activityViewController:itemForActivityType:];
-[DCActivityItemSource activityViewController:attachmentNameForActivityType:];
-[DCActivityItemSource attachmentTypeUTI];
-[DCActivityItemSource initWithDocumentInfoCollection:];
-[DCActivityItemSource docInfoCollection];
-[DCActivityItemSource setDocInfoCollection:];
```
