function Book(title, author, pages, read){
 this.title = title
 this.author = author
 this.pages = pages
 this.read = read
}
Book.prototype.theHobbit = function(){
    console.log(theHobbit.info());
}
theHobbit = Book("theHobbit", "J.R.R. Tolkien", "295", "not read yet" )
console.log(theHobbit.info());