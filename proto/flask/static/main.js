(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Skills
    $('.skill').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 25,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });
    
})(jQuery);


//
//



const videos = [
    {
        src: "https://www.youtube.com/embed/vtfMzmkYp9E?si=zsWZ2lTMk6fverfN",
        title: "Cyber Bullying",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/mqzP7gJDM2s?si=qT-oOWvo5daSUkDW",
        title: "Malware Attack",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/UvooremyBM4?si=osaHLdjg4vA5Kmz9",
        title: "Identity Theft",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/nfgflVnD7hE?si=5nSPsJm7vP0matJg",
        title: "Insider Threats",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/c1K6bw5ATzk?si=zg6QkR3zVpFCDL-s",
        title: "Data Breaches",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/BQc1d4RPIRs?si=aLpT7skeguPgbZxB",
        title: "Photo Morphing",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/BQc1d4RPIRs?si=aLpT7skeguPgbZxB",
        title: "Photo Morphing",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/BQc1d4RPIRs?si=aLpT7skeguPgbZxB",
        title: "Photo Morphing",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/BQc1d4RPIRs?si=aLpT7skeguPgbZxB",
        title: "Photo Morphing",
        description: "Digital Agency Website Design And Development"
    },
    {
        src: "https://www.youtube.com/embed/BQc1d4RPIRs?si=aLpT7skeguPgbZxB",
        title: "Photo Morphing",
        description: "Digital Agency Website Design And Development"
    }
];

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function displayVideos() {
    shuffleArray(videos);
    const videoContainer = document.getElementById('videoContainer');
    videoContainer.innerHTML = ''; // Clear previous content

    for (let i = 0; i < 6; i++) {
        const video = videos[i];
        const videoElement = `
            <div class="col-lg-4 col-md-6 portfolio-item first second wow fadeInUp" data-wow-delay="0.${i + 1}s">
                <div class="rounded overflow-hidden">
                    <div class="position-relative overflow-hidden">
                        <iframe width="560" height="315" src="${video.src}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                        <div class="portfolio-overlay">
                            <a class="btn btn-square btn-outline-light mx-1" href="${video.src}" target="_blank"><i class="fa fa-link"></i></a>
                        </div>
                    </div>
                    <div class="bg-light p-4">
                        <p class="text-primary fw-medium mb-2">${video.title}</p>
                        <h5 class="lh-base mb-0">${video.description}</h5>
                    </div>
                </div>
            </div>
        `;
        videoContainer.innerHTML += videoElement;
    }
}

// Change videos every 7 seconds
displayVideos();
setInterval(displayVideos, 5000);

