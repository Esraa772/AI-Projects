## Table of content
* [Introduction](#intro)
* [Try the model on local computer](#local_device_instalion)
* [Try the model on google colab](#google_colab)
* [Resources](#ref)


## Introduction
This is an image classification model based on [Teachable Machine](https://teachablemachine.withgoogle.com/)

### What is Teachable Machine?

![Teachable Machine](./readme_images/teachablemachine.gif)

[Teachable Machine](https://teachablemachine.withgoogle.com/) is a web-based tool that makes creating machine learning models fast, easy, and accessible for everyone. [You can try it here](https://teachablemachine.withgoogle.com/).

### Who is it for?
Educators, artists, students, innovators, makers of all kinds – really, anyone who has an idea they want to explore. No prerequisite machine learning knowledge required.

### How does it work?
You train a computer to recognize your images, sounds, and poses without writing any machine learning code. Then, use your model in your own projects, sites, apps, and more.
### steps:
<div class="block-holder">
  <div class="block">
    <div class="block-copy">
      <h4 class="numeral">https://github.com/Esraa772/AI-Projects
        <span class="numeral-no">1</span>
       . Gather
      </h4>
      <img height="200px" src="./readme_images/collect.svg" alt="Illustration of example cats">
      <p>
        Gather and group your examples into classes, or categories, that you want the computer to learn.
      </p>
      <a class="block-link" href="https://teachablemachine.withgoogle.com/train?action=onboardOpen&id=DFBbSTvtpy4">
        Video: Gather samples
      </a>
    </div>
  </div>
  <div class="block">
    <div class="block-copy">
      <h4 class="numeral">
         <span class="numeral-no">2</span>
       . Train
      </h4>
       <img height="200https://github.com/Esraa772/AI-Projectspx" src="./readme_images/train.svg" alt="Illustration of button being clicked that reads Train Model">
      <p>
        Train your model, then instantly test it out to see whether it can correctly classify new examples.
      </p>
      <a class="block-link" href="https://teachablemachine.withgoogle.com/train?action=onboardOpen&id=CO67EQ0ZWgA">
        Video: Train your model
      </a>
    </div>
  </div>
  <div class="block">
    <div class="block-copy">
      <h4 class="numeral">
         <span class="numeral-no">3</span>
       . Export
      </h4>
      <img height="200px" class="fullwidth" src="./readme_images/export.svg" alt="alt="Illustration of a desktop and mobile web browser containing a sample teachable machine project">
      <p>Export your model for your projects: sites, apps, and more. You can download your model or host it online for free.</p>
      <a class="block-link" href="https://teachablemachine.withgoogle.com/train?action=onboardOpen&id=n-zeeRLBgd0">
        Video: Export your model
      </a>
    </div>
  </div>
</div>

## Try the model on local computer 
### Libraries and dependencies 
To run this model on your local computer, you will need to install these libraries on whatever coding environment you will be using.
1. [cv2](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html)
2. [tensorflow Keras](https://keras.io/)
3. [PIL](https://readthedocs.org/projects/pil/downloads/pdf/latest/)
4. [numpy](https://numpy.org/)
5. [time](https://www.programiz.com/python-programming/time)
6. [os](https://www.geeksforgeeks.org/os-module-python-examples/)

After installing all needed libraries, toy can run the model using pictures from your local device or using your computer camera. if you are using external camera make sure that you have configured it right with your computer.

## Try the model on google colab
### what is [google colab](https://colab.research.google.com/notebooks/intro.ipynb#scrollTo=P-H6Lw1vyNNd)?
Colaboratory, or "Colab" for short, allows you to write and execute Python in your browser, with:
* Zero configuration required
* Free access to GPUs
* Easy sharing
Whether you're a student, a data scientist or an AI researcher, Colab can make your work easier. Watch [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI) to learn more.

With Colab you can import an image dataset, train an image classifier on it, and evaluate the model, all in just a few lines of code. Colab notebooks execute code on Google's cloud servers, meaning you can leverage the power of Google hardware, including GPUs and TPUs, regardless of the power of your machine. All you need is a browser.
### using Colab in Machine learning
Colab is used extensively in the machine learning community with applications including:
* Getting started with TensorFlow
* Developing and training neural networks
* Experimenting with TPUs
* Disseminating AI research
To see sample Colab notebooks that demonstrate machine learning applications, see the [machine learning examples](https://colab.research.google.com/notebooks/intro.ipynb#machine-learning-examples)

