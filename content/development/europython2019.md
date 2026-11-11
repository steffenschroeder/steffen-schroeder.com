Title: EuroPython 2019
Date: 2019-07-13
slug:europython-2019
Summary: A Summary of my impressions from EuroPython 2019 in Basel
Category: Development
Tags: Python, Conference

This year I attended my first EuroPython. It took place in Basel which is close to the place I live.

## Talks

I attended some talks. This is a personal summary for me. Maybe others find this helpful, too.

### Samuel Colvin - Python's Parallel Programming Possibilities - 4 levels of concurrency

Samuel showed 4 kinds of parallelism:

1. multiple (virtual) machines
2. multiple processes
3. multiple threads
4. asyncio

Main take-aways: Different kinds of parallelism require diff

He showed advantages and disadvantages. There is a great matrix in this talk of when to take which kind of parallelism.

<iframe width="560" height="315" src="https://www.youtube.com/embed/0RaotdCa_j0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Petr Stehlík - The dos and don'ts of task queues

Task queue help to separate work using producer-consumer pattern. One piece if coding is creating a task, another part is executing it.
Petr compared working RQ (Redis Queue) with Celery. While initial setup for RQ appears to be simple and Celery appears to be an overkill,
it quickly turned out that more and more code needs to be written for orchestrating RQ.
He and the colleagues at Kiwi, basically needed 4 week and 1000 lines of code to get the functionality they required.
Switching to Celery saved them a lot of boilerplate code.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gV01ZPxWuZg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Miroslav Šedivý -  A day has only 24±1 hours

Miro gave this talk a couple of times. I already saw it twice and there is always something new to learn.
He started explaining time zones, the usage in Python using _pytz_ and some common traps and pitfalls.
He continued with some interesting data analysis from [the IANA database](https://www.iana.org/time-zones).

He showed how this data set is an archive of modern history. Like the time zones in europe changes during the cause of
World War II.

<iframe width="560" height="315" src="https://www.youtube.com/embed/mHaz5laPyHE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Paul Everitt - Python 1994

Paul gave an extremely entertaining talk about the early days of python.
By showing some news group entries and just telling a lot of "funny stories", he took us through a very short-while
travel though the early days of the python community

<iframe width="560" height="315" src="https://www.youtube.com/embed/vyz7zdGiPVY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Raphael Pierzina - Advanced pytest

Raphael gave an overview on how the pytest plugin system works.
On the example of automatically adding markers to slow tests, Raphael showed how the pytest hooks work and how one can use this.

The talk is based on 2 blog posts _Customizing your pytest test suite_ (Part [1](https://raphael.codes/blog/customizing-your-pytest-test-suite-part-1/) & [2](https://raphael.codes/blog/customizing-your-pytest-test-suite-part-2/)).
I highly recommend watching the talk and reading the corresponding blog posts

<iframe width="560" height="315" src="https://www.youtube.com/embed/gJtE-anbcww" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
