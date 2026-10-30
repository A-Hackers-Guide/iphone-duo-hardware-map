# `ETDataSourceFromFolderData`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ETDataSource`
- 7 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _balanceClassesForTraining;
i _numberOfClasses;
@"NSString" _imagesDir;
@"NSMutableDictionary" _folderToImages;
@"NSArray" _imageFileNames;
@"NSMutableArray" _classNames;
@"NSMutableDictionary" _pathToClassIndex;
```

## Properties

```
@property (T@"NSString",&,N,V_imagesDir) imagesDir;
@property (T@"NSMutableDictionary",&,N,V_folderToImages) folderToImages;
@property (T@"NSArray",&,N,V_imageFileNames) imageFileNames;
@property (T@"NSMutableArray",&,N,V_classNames) classNames;
@property (T@"NSMutableDictionary",&,N,V_pathToClassIndex) pathToClassIndex;
@property (Ti,V_numberOfClasses) numberOfClasses;
@property (TB,V_balanceClassesForTraining) balanceClassesForTraining;
```

## Instance methods

```
-[ETDataSourceFromFolderData numberOfDataPoints];
-[ETDataSourceFromFolderData bufferWithPath:];
-[ETDataSourceFromFolderData numberOfClasses];
-[ETDataSourceFromFolderData balanceClassesForTraining];
-[ETDataSourceFromFolderData classNames];
-[ETDataSourceFromFolderData dataPointAtIndex:];
-[ETDataSourceFromFolderData folderToImages];
-[ETDataSourceFromFolderData imageFileNames];
-[ETDataSourceFromFolderData imagesDir];
-[ETDataSourceFromFolderData initWithFolder:balanceClassesForTraining:];
-[ETDataSourceFromFolderData pathToClassIndex];
-[ETDataSourceFromFolderData setBalanceClassesForTraining:];
-[ETDataSourceFromFolderData setClassNames:];
-[ETDataSourceFromFolderData setFolderToImages:];
-[ETDataSourceFromFolderData setImageFileNames:];
-[ETDataSourceFromFolderData setImagesDir:];
-[ETDataSourceFromFolderData setNumberOfClasses:];
-[ETDataSourceFromFolderData setPathToClassIndex:];
```
