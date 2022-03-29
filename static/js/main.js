/*************** CHANGE BACKGROUND HEADER ***************/
function scrollHeader() {
    const header = document.getElementById('header')

    if(this.scrollY >= 50) {
        header.classList.add('scroll-header')
    } else {
        header.classList.remove('scroll-header')
    }
}

window.addEventListener('scroll', scrollHeader)

/*************** Mobile Menu ***************/
const toggle = document.getElementById('nav__toggle')
const header = document.getElementById('header')

toggle.addEventListener('click', () => {
    if(header.style.height == '17em') {
        header.style.height = 'var(--header-height)'
        toggle.innerHTML = '<i class="fa-solid fa-bars"></i>'
    }else {
        header.style.height = '17em'
        toggle.innerHTML = '<i class="fa-solid fa-xmark"></i>'
    }
})

/*************** COURSES MODAL ***************/
const modalView = document.querySelectorAll('.courses__modal'),
      modalBtns = document.querySelectorAll('.courses__button'),
      modalClose = document.querySelectorAll('.courses__modal-close')

let modal = (modalClick) => {
    modalView[modalClick].classList.add('active-modal')
}

modalBtns.forEach((mb, i) => {
    mb.addEventListener('click', () => {
        modal(i)
    })
})

modalClose.forEach((mc) => {
    mc.addEventListener('click', () => {
        modalView.forEach((mv) => {
            mv.classList.remove('active-modal')
        })
    })
})


/*************** SWIPER TESTIMONIAL ***************/
let swiperTestimonial = new Swiper('.extra__data', {
    spaceBetween: 24,
    loop: true,
    grabCursor: true,

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    breakpoints: {
        567: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 48
        },
    },
})