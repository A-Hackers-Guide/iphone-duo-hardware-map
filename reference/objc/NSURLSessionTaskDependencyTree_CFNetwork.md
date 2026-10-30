# `NSURLSessionTaskDependencyTree`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 3 instance methods, 3 class methods

## Instance variables

```
@"NSURL" _mainDocumentURL;
```

## Properties

```
@property (T@"NSURL",&,N,V_mainDocumentURL) mainDocumentURL;
```

## Class methods

```
+[NSURLSessionTaskDependencyTree dependencyTreeDefaultWeb];
+[NSURLSessionTaskDependencyTree dependencyTreeWithJSONData:error:];
+[NSURLSessionTaskDependencyTree dependencyTreeWithMainDocumentURL:dependencyDescriptions:];
```

## Instance methods

```
-[NSURLSessionTaskDependencyTree mainDocumentURL];
-[NSURLSessionTaskDependencyTree setMainDocumentURL:];
-[NSURLSessionTaskDependencyTree dealloc];
```
